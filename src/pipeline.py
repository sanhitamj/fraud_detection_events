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

    def output_labelarray(self):
        """
        This function will return the response variable.

        OUTPUT:
            y - (numpy array) Boolean of Fraud (1) / Not Fraud (0)
        """
        return df['acct_type'].str.contains("fraud")



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
        """
        Adds new dummy variables

        Does not remove any original features
        """

        # Identifies short descriptions, which are strongly
        # correlated with fraudulent behavior.
        # Cutoff length was determined by graphing -TC
        cutoff_length = 23
        self.df['short_description'] = df['body_length'] < 23
        # This is automatically a boolean


    def _filter_features(self):
        features_to_keep = ['short_description',
                            'payout'
                           ]

        self.df = self.df[features_to_keep].copy()
