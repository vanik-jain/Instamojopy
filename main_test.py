import webtest

import main

import requests

import json

def test_index():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get('/')
    assert r.status_code == 200
assert 'Hello World' in r.data.decode('utf-8')

def test_get():
    app = webtest.TestApp(main.app)

    response = app.get('/')

    assert response.status_int == 200
    assert response.body == 'Hello, World!'


client_id = "CBzDgynYEWxICcKYHxWSQfUvoY5inUnQqqeFcICe"
client_secret = "TykXXhbl06Yp0ifGrsdWGabKeeBU5nhEC29ivceMhQpz78BM5AJ4l1G5ShfT3rYAcnndBfFvkOtCNjfsYUgUadoNW3FEYP1LVMIxfdmhdAZ9ZhmsBoSQGPeH1Q1ZGhA9"
env = "production"

if (client_id.startswith("test")):
    url = "https://test.instamojo.com/oauth2/token/"
    env = "test"

payload = "grant_type=client_credentials&client_id=" + client_id + "&client_secret=" + client_secret
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)
token = env + json.loads(response.text)["access_token"]
print(token)

