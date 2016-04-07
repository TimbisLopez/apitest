from flask import Flask, request

from functools import wraps
import types


def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if request.headers.get('apiKey') and request.headers.get('apiKey') == '12345678':
            return view_function(*args, **kwargs)
        else:
            return { 'error' : 'No apikey present' }
    return decorated_function

def api_route(self, *args, **kwargs):
    def wrapper(cls):
        self.add_resource(cls, *args, **kwargs)
        return cls
    return wrapper
