from functools import wraps
from flask import request, Response, abort


def check_auth(key):
    return key == "helloworld"


def requires_key_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.args.get('apikey', '')
        if not key or not check_auth(key):
            return abort(401)
        return f(*args, **kwargs)

    return decorated
