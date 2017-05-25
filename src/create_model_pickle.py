"""
RUN THIS FILE FROM SRC

    # Fit models (ONE TIME USE)
    models = [tyler_logit_model]
    model_names = ["tyler_logit"]
    for model, name in zip(models, model_names):
        currentmod = model()
        currentmod.fit(relative_dir)


    ### API LINES FOR PREDICTION
    #Logit Model
    tlm = tyler_logit_model()
    tlm.predict(json_data, threshold=0.3)
"""
from request_json import get_json
import random
import cPickle as pickle
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import normalize, scale, StandardScaler
from pipeline import pipeline_json
import os
import numpy as np


class tyler_logit_model():
    """Pipelines test data and fits to an object"""
    def __init__(self):
        self.scaler_loc = "../models/logit_scaler.pkl"
        self.lrmodel = "../models/logit_model.pkl"

    def fit(self, data):
        """Fits an external json or path"""

        X, y = self._pipe_data(data, response=True)
        lr = LogisticRegression(class_weight='balanced', n_jobs=-1, C=0.1)
        lr.fit(np.array(X), np.array(y))

        with open(self.lrmodel, 'w') as f:
            pickle.dump(lr, f)


    def predict(self, data, threshold=0.5):
        with open(self.scaler_loc, 'r') as f:
            scaler = pickle.load(f)

        X = self._pipe_data(data, response=False, scaler_exists=True)

        with open(self.lrmodel, 'r') as f:
            lr = pickle.load(f)
        print lr

        prob = lr.predict_proba(X)[:, 1]

        return prob, (prob > threshold)




    def _pipe_data(self, data, response=False, scaler_exists=False):

        if scaler_exists:
            with open(self.scaler_loc, 'r') as f:
                scaler = pickle.load(f)
            pj = pipeline_json(data, scaler=scaler)
        else:
            pj = pipeline_json(data)

        X = pj.convert_to_df(scaling=True, filtered=True)

        with open(self.scaler_loc, 'w') as f:
            pickle.dump(pj.scaler, f)

        if response:
            y = pj.output_labelarray()
            return X, y
        return X




if __name__ == '__main__':
    relative_dir = "../data/data.json"
    direc = os.path.dirname(__file__)
    filename = os.path.join(direc, relative_dir)


    # Fit models (ONE TIME USE)
    # models = [tyler_logit_model]
    # model_names = ["tyler_logit"]
    # for model, name in zip(models, model_names):
    #     currentmod = model()
    #     currentmod.fit(relative_dir)


    ### API LINES FOR PREDICTION
    #Logit Model
    tlm = tyler_logit_model()
    json_str = get_json()
    tlm.predict(json_str, threshold=0.3)
