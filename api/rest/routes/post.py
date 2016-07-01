from flask_restful import Resource

## Rest Controller Layer should only handle HTTP responses/requests and JSON serilization/deserilization.

class PostContent(Resource):
	method_decorators = [auth_token_required]
	#Method decorator to check if incomming request has an auth token in the header or not.
	def post(self):
		data = request.get_json()
		jwt_token = str(request.headers.get('JWT-Auth'))
		payload = jwt.decode(jwt_token, signkey, algorithms=['HS512']) #Decoding JWT token
		jwt_id = payload['uuid'] #Getting id in payload of JWT to ensure people cant upload referencing other peoples usernames 

		response, status = Post.post(data, jwt_id)
		return Response(response=response, status=status, mimetype='application/json')

	def get(self, id):
		response, status = Post.get(id)
		return Response(response=response, status=status, mimetype='application/json')