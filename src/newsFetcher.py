import os
import pandas as pd
from newsapi import NewsApiClient
from src.enums import Country, SortBy


class NewsFetcher:
    def __init__(self, api_key=None):
        self.api = NewsApiClient(api_key=api_key or os.environ["NEWS_API_KEY"])

    def get_media_sources(self, country, *args, **kwargs):
        if not isinstance(country, Country):
            raise Exception("Invalid country")

        sources = self.api.get_sources(country=country, *args, **kwargs)
        return pd.DataFrame(sources["sources"])

    def get_articles(self, topic, media_sources: list = None, sort_by=SortBy.RELEVANCY, max_per_source=5, *args, **kwargs):
        """Get articles from diverse sources in a country."""
        if not isinstance(sort_by, SortBy):
            raise Exception("Invalid country")

        articles = self.api.get_everything(
            q=topic,
            sources=','.join(media_sources),
            sort_by=sort_by,
            page_size=len(media_sources) * max_per_source
        )

        return pd.json_normalize(articles["articles"])