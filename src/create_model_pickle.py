import random
import cPickle as pickle

class MyModel():
    def fit():
        pass
    def predict():
        return random.choice([True, False])

def get_data(datafile):
    pass
    return X, y

if __name__ == '__main__':
    X, y = get_data('files/data.json')
    model = MyModel()
    model.fit(X, y)
    with open('model.pkl', 'w') as f:
        pickle.dump(model, f)
