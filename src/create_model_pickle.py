import random
import cPickle as pickle
from sklearn.linear_model import LogisticRegression
from src.pipeline import pipeline_json


class tyler_logit_model():
    """Pipelines test data and fits to an object"""
    def __init__(self):
        pass

    def fit(X, y):
        """Fits an external json or path"""

        X, y = self._pipe_data(X, y)
        lr = LogisticRegression(X, y)
        lr.fit(X, y)

        self.model = lr


    def predict(X, threshold=0.5):
        return self.model.predict_proba(X_test)[:, 1] > threshold

    def _pipe_date(X, y=None):
        pj = pipeline_json('../data/data.json')
        df = pj.convert_to_df(scaling=True, filtered=True)

        X = pj.convert_to_df(scaling=True, filtered=True)

        if y:
            y = pj.output_labelarray()

        return X, y

def get_data(datafile):
    pass
    return X, y

if __name__ == '__main__':
    X, y = get_data('data/data.json')

    # Dump all listed models to the model folder
    models = [tyler_logit_model]
    for model in models:
        currentmod = model()
        model.fit(X, y)
        model_name = "models/" + type(model).__name__ + ".pkl"
        with open(model_name, 'w') as f:
            pickle.dump(model, f)
