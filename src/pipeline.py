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
import numpy as np

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
        # self._filter_features() IMPLEMENT THIS AT THE END

        return self.df.copy()

    def output_labelarray(self):
        """
        This function will return the response variable.

        OUTPUT:
            y - (numpy array) Boolean of Fraud (1) / Not Fraud (0)
        """
        return self.df['fraud']

    def _convert_datetime(self):
        # Wallace edit
        # Convert date columns to datetime format
        date_cols = ['approx_payout_date', 'event_created', 'event_created', 'event_end', \
                     'event_published', 'event_start', 'user_created']
        for col in date_cols:
            self.df[col] = pd.to_datetime(self.df[col])

    def _convert_bools(self):
        bin_dict = {0 : False, 1 : True}
        bin_cols = ['show_map', 'fb_published', 'has_logo', 'has_analytics']
        for col in bin_cols:
            self.df[col] = self.df[col].map(bin_dict)

        yn_dict = {'y': 1, 'n' : 0}
        yn_cols = ['listed']
        for col in yn_cols:
            self.df[col] = self.df[col].map(yn_dict)

        bin_nan_cols = ['has_header']
        for col in bin_nan_cols:
            self.df[col] = self.df[col].map(lambda x: x if not np.isnan(x) else -1)
            self.df[col].astype('int', copy=True)

        payout_dict = {'CHECK': 1, 'ACH' : 1, '':0}
        self.df['payout_type'] = self.df['payout_type'].map(payout_dict)

    def _add_features(self):
        """
        Adds new dummy variables

        Does not remove any original features
        """

        #Condition Response variable fraud flag
        self.df['fraud'] = self.df['acct_type'].str.contains("fraud")

        # Identifies short descriptions (strong fraud correlation).
        cutoff_length = 23
        self.df['short_description'] = self.df['body_length'] < 23


    def _filter_features(self):
        features_to_keep = ['short_description',
                            'payout'
                           ]

        self.df = self.df[features_to_keep].copy()
