"""
Creates a pipelined dataframe to
local notebook

------------

EXAMPLE USE IN NOTEBOOK:

from src.pipeline import pipeline_json
pj = pipeline_json(json_dir)
df = pj.convert_to_df(json_dir)


-Tyler
"""

import pandas as pd

class pipeline_json(object):

    def __init__(self, json_dir="../data/data.json"):
        self.df = pd.read_json(json_dir)

    def convert_to_df(self, json=None):
        if json:
            self.df = pd.read_json(json_dir)

        self._convert_datetime()
        self._add_features()
        self._filter_features()

        return self.df.copy()

    def _convert_datetime(self, df):
        # Wallace

        pass

    def _add_features(self):

        # Add 'short_description' feature -t

        pass

    def _filter_features(self):
        pass
