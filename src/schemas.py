from pydantic import BaseModel, Field
from typing import List


class BiasAnalysisOutput(BaseModel):
    """Structured bias analysis output"""

    sensationalism_score: int = Field(description="Is it clickbait? --> 0-10 scale. 0=dry facts, 10=extreme clickbait", ge=0, le=10)
    emotional_charge: int = Field(description="Is it trying to make you angry/happy? --> 0-10 scale. 0=neutral, 10=highly emotional", ge=0, le=10)
    political_leaning: str = Field(description="Perceived leaning: 'Left', 'Right', 'Center', or 'Neutral'")
    sentiment: str = Field(description="Overall sentiment: 'Positive', 'Negative', or 'Neutral'")

    # Detailed analysis
    bias_indicators: List[str] = Field(description="Specific words/phrases that indicate bias", default=[])
    framing: str = Field(description="How is the story framed? What perspective is emphasized?")
    subjectivity_flag: bool = Field(description="True if contains opinionated language")

    # Explanation
    reasoning: str = Field(description="2-3 sentence explanation of the analysis")


class ComparativeBiasAnalysisOutput(BaseModel):
    """For comparing multiple headlines"""

    headlines_analyzed: int
    most_sensational: str
    most_neutral: str
    political_spectrum_summary: str
    key_differences: List[str]
