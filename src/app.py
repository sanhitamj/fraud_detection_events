from flask import Flask, url_for, render_template, request
from create_model_pickle import tyler_logit_model
from store_sql import insert_vals, read_vals
import numpy as np
import json

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Flask root'

#define website
@app.route('/hello', methods=['GET'])   #map web page to address with decorator
def hello():
    return 'Hello, World!'

#define website
@app.route('/score', methods=['GET', 'POST'])   #map web page to address with decorator
def score():
    json_input = request.get_json()
    tlm = tyler_logit_model()
    prob, prediction = tlm.predict(json_input)


    insert_vals(prob.astype(np.float64),
                prediction.astype(int),
                '{}'.format(json_input),
                user='tyler'
               )

    return render_template('score.html', name=prediction)

#DEBUG - WHAT WAS LAST POST??
@app.route('/scoredebug', methods=['GET', 'POST'])   #map web page to address with decorator
def scoredebug():
    sqlbase = read_vals(user='tyler')
    # jd = json.JSONDecoder()
    sqlbase = [x[3] for x in sqlbase]
    print sqlbase
    # indices = [x[0] for x in sqlbase]
    # probas = [x[1] for x in sqlbase]
    # fraud_flags = [x[2] for x in sqlbase]
    # event_names = [x[3] for x in sqlbase]
    # org_names = [x[4] for x in sqlbase]
    return render_template('score.html', name=sqlbase)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
