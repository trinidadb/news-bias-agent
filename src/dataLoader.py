import pandas as pd
from pathlib import Path
from functools import lru_cache


class NewsDataLoader:
    def __init__(self, data_path):
        self.data_path = Path(data_path)
        self.data = self._load_data()

    def _load_data(self):
        """Load the JSON lines file into a DataFrame"""
        return pd.read_json(self.data_path, lines=True)

    @lru_cache
    def get_sample(self, n=10, category=None, random_state=42):
        """Get a sample of articles"""
        if category:
            filtered = self.data[self.data['category'] == category]
            return filtered.sample(n=min(n, len(filtered)), random_state=random_state)
        return self.data.sample(n=min(n, len(self.data)), random_state=random_state)

    def get_high_bias_categories(self, n=10):
        """Get samples from categories likely to show bias"""
        categories = ['POLITICS', 'WORLD NEWS', 'BUSINESS', 'MEDIA']
        filtered = self.data[self.data['category'].isin(categories)]
        return filtered.sample(n=min(n, len(filtered)))

    def get_by_category(self, category):
        """Get all articles from a category"""
        return self.data[self.data['category'] == category]

    def to_dict_list(self, df_subset):
        """Convert DataFrame to list of dicts for analysis"""
        return df_subset[['headline', 'short_description', 'category']].to_dict('records')
