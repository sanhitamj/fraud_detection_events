"""
Loads a pickled model object from src folder.

Can be used to create a prediction on new data

INPUT:
    event - (See Features)

OUTPUT:
    label to STDOUT
"""

import cPickle as pickle
from src.create_model_pickle import tyler_logit_model
from sklearn.linear_model import LogisticRegression


if __name__ == "__main__":
    with open('models/tyler_logit.pkl') as f:
        up = pickle.Unpickler(f)
        model = up.load()
    print "model"
    print model
    print "type model"
    print type(model)

    # model = model()

    data_path = "data/data.json"

    y_pred = model.predict(data_path, 0.3)
    print "Score: {}".format((y_test == 1).mean(axis=1)) #test to see ratio
