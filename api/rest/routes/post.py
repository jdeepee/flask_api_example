from flask_restful import Resource

## Rest Controller Layer should only handle HTTP responses/requests and JSON serilization/deserilization.

class PostContent(Resource):
	method_decorators = [auth_token_required]
	#Method decorator to check if incomming request has an auth token in the header or not.
	def post(self):
		pass

	def get(self, id):
		pass