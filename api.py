from flask import Flask, request
from flask_restful import Resource, Api
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from functools import wraps
import types
app = Flask(__name__)
api = Api(app)
limiter = Limiter(app, key_func=get_remote_address)

def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if request.args.get('key') and request.args.get('key') == '12345678':
            return view_function(*args, **kwargs)
        else:
            return
    return decorated_function

def api_route(self, *args, **kwargs):
    def wrapper(cls):
        self.add_resource(cls, *args, **kwargs)
        return cls
    return wrapper

api.route = types.MethodType(api_route, api)


@api.route('/v1/')
class HelloWorld(Resource):
    decorators = [require_appkey, limiter.limit("3/day")]
    def get(self):
        return {
        	'status':'OK',
        	'data': [ 
        		{'hello': 'world'}
        	]
        }

@limiter.request_filter
def ip_whitelist():
    return request.remote_addr == "127.0.0.1"

if __name__ == '__main__':
    app.run(debug=True)