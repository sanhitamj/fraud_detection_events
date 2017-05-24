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

from sklearn.preprocessing import normalize, scale, StandardScaler
import pandas as pd
import numpy as np

class pipeline_json(object):

    def __init__(self, json_dir="../data/data.json"):
        self.orig_df = pd.read_json(json_dir)

    def convert_to_df(self, scaling=False):
        #Avoid re-reading JSON file every time conversion is done by copying original dataframe.
        self.df = self.orig_df.copy()

        #Start feature engineering:
        self._convert_datetime()
        self._convert_bools()
        self._add_features()
        # self._filter_features() IMPLEMENT THIS AT THE END

        if scaling:
            self._scale()

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
            self.df[col] = pd.to_datetime(self.df[col], unit='s')

    def _convert_bools(self):
        bin_dict = {0 : False, 1 : True}
        bin_cols = ['show_map', 'fb_published', 'has_logo', 'has_analytics']
        for col in bin_cols:
            self.df[col] = self.df[col].map(bin_dict)

        yn_dict = {'y': 1, 'n' : 0}
        yn_cols = ['listed']
        for col in yn_cols:
            self.df[col] = self.df[col].map(yn_dict)

        bin_nan_cols = ['has_header', 'org_facebook', 'org_twitter']
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


        # Account life of accounts
        df['account_life'] = df['event_created'] - df['user_created']
        df['account_life'] = df['account_life'].dt.days

        #Columns for payout : total amount, number of payouts, set(payee names)
        tot_payout_amt = []
        pay_cnt = []
        payees_list = []
        for i in xrange(self.df.shape[0]):
            total_payout = 0
            payout_count = len(self.df['previous_payouts'][i])
            payees = set()
            if payout_count > 0:
                for d in self.df['previous_payouts'][i]:
                    total_payout += d['amount']
                    payees.add(d['name'])
                tot_payout_amt.append(total_payout)
                pay_cnt.append(payout_count)
                payees_list.append(payees)
            else:
                tot_payout_amt.append(0)
                pay_cnt.append(payout_count)
                payees_list.append(set())
        self.df['total_payout'] = tot_payout_amt
        self.df['payout_count'] = pay_cnt
        self.df['payees_set'] = payees_list


    def _scale(self):

        features = ['org_facebook',
                    'has_analytics',
                    'org_twitter',
                    'account_life'
                   ]

        for feature in features:
            ss = StandardScaler()
            self.df[feature] = ss.fit_transform(self.df[feature])





    def _filter_features(self):
        features_to_keep = ['short_description',
                            'payout_type',
                            'fb_published',
                            'org_facebook',
                            'has_analytics',
                            'has_header',
                            'org_twitter',
                            'account_life'
                           ]

        self.df = self.df[features_to_keep].copy()
