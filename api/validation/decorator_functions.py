import jwt
from functools import wraps 

## Validation layer check incoming requests to see if they are valid before handling with the rest controller layer.

def auth_token_required(f): #Wrapping function to check and decode JWT token
	@wraps(f)
	def decorated_function(*args, **kwargs):	
		try:
			if not request.headers.get("JWT-Auth"): #Check for token
				response = json_message("Missing auth token")
				return Response(response=response, status=401, mimetype='application/json')
			else:
				token = request.headers.get("JWT-Auth")
				str_token = str(token)
				payload = jwt.decode(str_token, signkey, algorithms=['HS512']) #Decoding token
				uuid = payload['uuid']

				return f(*args, **kwargs) #Returning function

		except jwt.DecodeError: #If JWT token doesnt decode ie isnt created with same secret 
			response = json_message("Token is invalid")
			return Response(response=response, status=401, mimetype='application/json')

		except jwt.ExpiredSignature: #If JWT token has expired
			response = json_message("Token has expired, please sign in again")
			return Response(response=response, status=401, mimetype='application/json')

		return f(*args, **kwargs)
	return decorated_function


def json_included_authtoken(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		data = request.get_json()
		if data:
			try:
				data['username']
				data['password']

				if len(username) > 20:
					response = json_message("Username is too long")
					return Response(response=response, status=400, mimetype='application/json')

				return f(*args, **kwargs)
			except KeyError:
				response = json_message("You are missing some JSON fields")
				return Response(response=response, status=400, mimetype='application/json')

		else:
			response = json_message("You are missing JSON")
			return Response(response=response, status=400, mimetype='application/json')

		return f(*args, **kwargs)
	return decorated_function

def json_included_user(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		return f(*args, **kwargs)

	return decorated_function

