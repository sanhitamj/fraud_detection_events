'''
The function get_json will perform a GET request to the Galvanize API point and return the content of the JSON response as a string.

'''

import requests

def get_json():
  response = requests.get('http://galvanize-case-study-on-fraud.herokuapp.com/data_point')
  return response.json()
