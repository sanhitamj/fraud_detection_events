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
    tot_payout = sum([previous['amount'] for previous in json_input['previous_payouts']])
    risk_score = (float(tot_payout) * float(prob))

    insert_vals(round(float(prob), 4), # From model
                int(prediction), # From model
                unicode(json_input['org_name']), # From JSON
                unicode(json_input['name']),
                float(tot_payout),
                float(risk_score),
                '{}'.format(json_input),
                user='tyler'
               )

    return render_template('score.html', name=prediction)

#DEBUG - WHAT WAS LAST POST??
@app.route('/scoredebug', methods=['GET', 'POST'])   #map web page to address with decorator
def scoredebug():
    sqlbase = read_vals(user='tyler')
    headers = [
               "risk_score",
               "probability",
               "predict",
               "org_name",
               "name",
               "tot_payout"
              ]
    print type(sqlbase)
    for elem in sqlbase[0]:
        print type(elem)

    return render_template('score.html', name=sqlbase, headers=headers)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
