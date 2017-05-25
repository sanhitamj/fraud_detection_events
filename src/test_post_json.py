import requests
import json
from request_json import get_json


url = "http://127.0.0.1:5000/score"


r = requests.post(url, json=get_json())
# print r.text
