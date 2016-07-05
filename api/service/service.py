from ..repository.repository import *
from ..rest.functions.functions import *
from passlib.hash import bcrypt

## Service layer does most of the logic for your API and offloads any database transaction to the repository layer.
class User():
	def authtoken(username, password):
		exsist = UserRepository.does_exsist(username)

		if exsist == 1:
			response = json_message("There is no such user")
			return response, 400

		else:
			user_password = get_password_username(username)

			if bcrypt.verify(str(password), user_password): #Checking both passwords to see if they match(salted)
				uuid = str(get_user_id(username))

				payload = {"iat": datetime.now(), "uuid": uuid, "username": username, 'exp': datetime.now() + timedelta(days=60)} #Creating JWT payload
				encode = jwt.encode(payload, signkey, algorithm='HS512') #Encoding JWT token 
				utf_jwt = encode.decode('utf-8')
				json1 = {"JWT": utf_jwt, "id": uuid}

				return json1, 201

			else:
				response = json_message("Incorrect credentials")
				return response, 400

	def signup(data):
		username = data['username']
		password = bcrypt.encrypt((str(data['password'])))

		exsist = UserRepository.does_exsist(username)

		if exsist == 1:
			response = json_message("There is already a user with that username!")
			return response, 400


		else:
			UserRepository.signup(username, password)
			response = json_message("You have created a new account!")
			return response, 201

	def get(id):
		user_info = get_userinfo_username(id)
		if user_info:
			response = UsersSchema.dump(user_info)
			response = jsonify(response)
			return response, 200

		else:
			response = json_message("No such user")
			return response, 400

class Post():
	def post(data, id):
		post = data['post']
		post_id = uuid.uuid4()

		insert = PostRepository.post(post_id, user_id, post)

		if insert == 1:
			response = json_message("Successfully posted")
			return response, 201

		else:
			response = json_message("Something went wrong")
			return response, 400

	def get(id):
		data = PostRepository.get(id)
		if data:
			response = PostSchema.dump(data)
			response = jsonify(response)
			return response, 200

		else:
			response = json_message("There is no such post")
			return response, 400

