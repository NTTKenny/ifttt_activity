import requests

data = {'test ': ' test'}
url = 'https://maker.ifttt.com/trigger/activity/json/with/key/PmpaoECThG_JxEXrJ4AK9IUGvSePYG9H4cV0jCl777'

requests.post(url, data)