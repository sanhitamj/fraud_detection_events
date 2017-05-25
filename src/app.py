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
    dataframe = tlm.X_temp
    tot_payout = dataframe['total_payout']
    risk_score = (tot_payout * prob)

    insert_vals(float(prob), # From model
                int(prediction), # From model
                json_input['org_name'], # From JSON
                json_input['name'],
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
    headers = ["probability",
               "predict",
               "org_name",
               "name",
               "tot_payout",
               "risk_score",
               "json_str"
              ]

    return render_template('score.html', name=sqlbase, headers=headers)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
