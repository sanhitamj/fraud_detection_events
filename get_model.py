"""
Loads a pickled model object from src folder.

Can be used to create a prediction on new data

INPUT:
    event - (See Features)

OUTPUT:
    label to STDOUT
"""


import cPickle as pickle

with open('model.pkl') as f:
    model = pickle.load(f)

model.predict()
