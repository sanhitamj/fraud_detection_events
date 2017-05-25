"""
RUN THIS FILE FROM SRC
"""

import random
import cPickle as pickle
from sklearn.linear_model import LogisticRegression
from pipeline import pipeline_json
import os
import numpy as np


class tyler_logit_model():
    """Pipelines test data and fits to an object"""
    def __init__(self):
        self.model = None

    def fit(self, data):
        """Fits an external json or path"""

        X, y = self._pipe_data(data, response=True)
        lr = LogisticRegression()
        lr.fit(np.array(X), np.array(y))

        self.model = lr


    def predict(self, data, threshold=0.5):
        X = self._pipe_data(data, response=False)
        return self.model.predict_proba(X)[:, 1] > threshold

    def _pipe_data(self, data, response=False):
        pj = pipeline_json(data)
        X = pj.convert_to_df(scaling=True, filtered=True)
        if response:
            y = pj.output_labelarray()
            return X, y
        return X


if __name__ == '__main__':
    relative_dir = "../data/data.json"
    direc = os.path.dirname(__file__)
    filename = os.path.join(direc, relative_dir)


    # Dump all listed models to the model folder
    models = [tyler_logit_model]
    model_names = ["tyler_logit"]
    for model, name in zip(models, model_names):
        currentmod = model()
        currentmod.fit(relative_dir)
        model_name = "../models/" + name + ".pkl"
        with open(model_name, 'w') as f:
            pickle.dump(model, f)
