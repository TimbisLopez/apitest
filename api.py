from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_limiter import Limiter

from decorators import * 
from utils import *
from models import *

app = Flask(__name__)

api = Api(app)
api.route = types.MethodType(api_route, api)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:tiger@localhost/mydatabase'
db = SQLAlchemy(app)

limiter = Limiter(app, key_func=get_apikey)
limite_compartido = limiter.shared_limit("100/hour", scope="all")

@api.route('/v1/')
class Hello(Resource):
    decorators = [require_appkey, limite_compartido]
    def get(self):
        return {
        	'status':'OK',
        	'data': [ 
        		{'hello': 'world'},
        	]
        }

@limiter.request_filter
def ip_whitelist():
    return request.remote_addr == "127.0.0.1"

@app.errorhandler(429)
def ratelimit_handler(e):
    return make_response(
            jsonify(error="ratelimit exceeded %s" % e.description)
            , 429
    )

if __name__ == '__main__':
    app.run(debug=True)