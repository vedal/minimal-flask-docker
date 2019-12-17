import simplejson as json
import requests


def post():

    url = 'http://0.0.0.0:8000/predict'
    message = {'key': 'value'}

    r = requests.post(url, json=message)
    print(r.json())

if __name__ == '__main__':
    post()