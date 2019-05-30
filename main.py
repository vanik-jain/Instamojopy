from flask import Flask
import requests

import json

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
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

    response = requests.request("POST", "https://api.instamojo.com/oauth2/token/", data=payload, headers=headers)
    token = env + json.loads(response.text)["access_token"]

    return token




if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
