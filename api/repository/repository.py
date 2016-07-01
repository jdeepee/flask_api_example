from ..database.database_model import *

## Repository layer will handle database transactions.
class UserRepository():
	def signup(username, password):
		data = User(username=username, password=password)
		try:
			db.session.add(data)
			db.session.commit()

		except:
			db.session.rollback()
			response = json_message("Sign up failed, please try again")
			return Response(response=response, status=500, mimetype='applicaton/json')
			raise

		finally:
			db.session.close()

		return 1

	def get_userinfo_id(id):
		return User.query.filter_by(id=id).first()

	def get_userinfo_username(username):
		return User.query.filter_by(username=username).first()

	def does_exsist(username):
		return User.query.filter_by(username = username).first()

	def get_password_username(username):
		data = User.query.filter_by(username=username).first()

		if data is None:
			return None

		else:
			return data.password

	def get_password_id(id):
		data = User.query.filter_by(id=id).first()

		if data is None:
			return None

		else:
			return data.password 

	def get_user_id(username):
		data = User.query.filter_by(username=username).first()

		if data is None:
			return None 

		else:
			return data.id

class PostRepository():
	def post(id, user_id, post):
		data = Post(id=id, user_id=user_id, post=post)
		try:
			db.session.add(data)
			db.session.commit()

		except:
			db.session.rollback()
			response = json_message("Posting content failed")
			return Response(response=response, status=400, mimetype='applicaton/json')
			raise

		finally:
			db.session.close()

		return 1

	def get(id):
		data = Post.query.filter_by(id=id).first()

		if data is None:
			return None

		else:
			return data
