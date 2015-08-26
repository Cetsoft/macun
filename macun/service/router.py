from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from macun.service.basic_auth import requires_auth
from macun.service.api_auth import requires_key_auth


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route("/")
@requires_auth
def index():
    return "Hello World"


@app.route("/key")
@requires_key_auth
def key():
    return "Hello World"
