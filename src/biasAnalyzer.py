from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableConfig
from typing import List, Dict
from src.schemas import BiasAnalysisOutput


class BiasAnalyzer:
    def __init__(self, system_prompt, model_name="gemini-2.5-flash", temperature=0.3, max_retries=2):
        self.llm = ChatGoogleGenerativeAI(
            model=model_name,
            temperature=temperature,
            max_retries=max_retries
        )

        self.structured_llm = self.llm.with_structured_output(BiasAnalysisOutput)

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "Headline: {headline}\n\nDescription: {description}")
        ])

        self.chain = self.prompt | self.structured_llm

    def _error_response(self, error_msg: str) -> BiasAnalysisOutput:
        return BiasAnalysisOutput(
                sensationalism_score=0,
                emotional_charge=0,
                political_leaning="Unknown",
                sentiment="Neutral",
                bias_indicators=[],
                framing="Error in analysis",
                subjectivity_flag=False,
                reasoning=f"Analysis failed: {error_msg}"
            )

    def analyze_news(self, headline: str, description: str = "") -> BiasAnalysisOutput:
        try:
            result = self.chain.invoke({
                "headline": headline,
                "description": description or "No description provided"
            })
            return result
        except Exception as e:
            print(f"Error analyzing: {e}")
            return self._error_response(str(e))

    def analyze_news_batch(self, articles: List[Dict], max_concurrency: int = 5) -> List[BiasAnalysisOutput]: # TODO: consider using num_cores = os.cpu_count() as the value for max_concurrency
        inputs = [
            {
                "headline": article.get('headline', ''),
                "description": article.get('description', article.get('short_description', ''))
            }
            for article in articles
        ]

        try:
            config = RunnableConfig(max_concurrency=max_concurrency)
            results = self.chain.batch(inputs, config=config) # TODO: consider using "abatch" (async) when maximum performance needed or when running in an async environment (e.g., FastAPI)
            return results
        except Exception as e:
            print(f"Batch processing error: {e}. Fallback to sequential.")
            return [self.analyze_news(inp['headline'], inp['description']) for inp in inputs]

    def analyze_news_batch_streaming(self, articles: List[Dict], max_concurrency: int = 5):
        inputs = [
            {
                "headline": article.get('headline', ''),
                "description": article.get('description', article.get('short_description', ''))
            }
            for article in articles
        ]

        config = RunnableConfig(max_concurrency=max_concurrency)

        # batch_as_completed returns results as they finish
        for result in self.chain.batch_as_completed(inputs, config=config):
            yield result

    def get_summary_stats(self, results: list) -> dict:
        """Get aggregate statistics from multiple analyses"""
        if not results:
            return {}

        sum_sensationalism, sum_emotional_charge, sum_subjectivity_rate = 0, 0, 0
        political_counts = {"Left": 0, "Right": 0, "Center": 0, "Neutral": 0}
        for r in results:
            sum_sensationalism += r.sensationalism_score
            sum_emotional_charge += r.emotional_charge
            sum_subjectivity_rate += (1 if r.subjectivity_flag else 0)
            if r.political_leaning in political_counts:
                political_counts[r.political_leaning] += 1

        total_items = len(results)

        return {
            "avg_sensationalism": sum_sensationalism / total_items,
            "avg_emotional_charge": sum_emotional_charge / total_items,
            "political_distribution": political_counts,
            "subjectivity_rate": sum_subjectivity_rate / total_items,
            "total_analyzed": total_items
        }
