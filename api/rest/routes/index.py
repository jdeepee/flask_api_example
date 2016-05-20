from flask_restful import Resource
from ..functions.function import json_message

## Rest Controller Layer should only handle HTTP responses/requests and JSON serilization/deserilization.

class index(Resource):
	#All HTTP get requests to '/' are handled by this function
	def get(self):
		response = json_message("Example Flask Application")
		return Response(response=response, status=200, mimetype='application/json')