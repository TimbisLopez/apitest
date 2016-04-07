from flask import request


def get_apikey():
	return request.headers.get('apiKey')