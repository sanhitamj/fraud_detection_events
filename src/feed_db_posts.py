import requests
import json
from request_json import get_json
from time import sleep


if __name__ == "__main__":
    for i in xrange(10000):
        url = "http://127.0.0.1:5000/score"
        r = requests.post(url, json=get_json())
        sleep(15)
