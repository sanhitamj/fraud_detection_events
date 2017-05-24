"""
Creates a pipelined dataframe to
local notebook

------------

EXAMPLE USE IN NOTEBOOK:

from src.pipeline import pipeline_json
pj = pipeline_json('../data/data.json')
df = pj.convert_to_df()


-Tyler
"""

import pandas as pd

class pipeline_json(object):

    def __init__(self, json_dir="../data/data.json"):
        self.orig_df = pd.read_json(json_dir)

    def convert_to_df(self):
        #Avoid re-reading JSON file every time conversion is done by copying original dataframe.
        self.df = self.orig_df.copy()

        #Start feature engineering:
        self._convert_datetime()
        self._convert_bools()
        self._add_features()
        self._filter_features()

        return self.df.copy()

    def _convert_datetime(self):
        # Wallace edit
        # Convert date columns to datetime format
        date_cols = ['approx_payout_date', 'event_created', 'event_created', 'event_end', \
                     'event_published', 'event_start', 'user_created']
        for col in date_cols:
            self.df[col] = pd.to_datetime(self.df[col])

    def _convert_bools(self):
        pass

    def _add_features(self):
<<<<<<< HEAD

        # Add 'short_description' feature -t

=======
>>>>>>> 52bbcbb157940890a9df2af6ccaa84e63e5c02de
        pass

    def _filter_features(self):
        pass
