from flask_restful import Resource
from ..service.service import *

## Rest Controller Layer should only handle HTTP responses/requests and JSON serilization/deserilization.

class User(Resource):
	def post(self):
		data = request.get_json()

		response, status = User.signup(data)
		return Response(response=response, status=status, mimetype='application/json')

class UserGet(Resource):
	#All HTTP get requests to '/users/<id>/' are handled by this function. Notice the id in the function parameters.
	def get(self, id):
		response, status = User.get(id)
		return Response(response=response, status=status, mimetype='application/json')

class AuthToken(Resource):
	#All HTTP post request to '/authtoken/' are handled by this function.
	method_decorators = [json_included_authtoken]

	def post(self):
		data = request.get_json()
		username = data['username']
		password = data['password']

		response, status = User.authtoken(username, password)
		return Response(response=response, status=status, mimetype='application/json')

