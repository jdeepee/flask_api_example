from ..database.database_model import *

## Repository layer will handle database transactions.

class UserRepository():
	def signup():
		pass

	def get_userinfo_id(id):
		pass

	def get_userinfo_username(username):
		pass

	def does_exsist(username):
		check = db.session.query(User).filter(User.username == username).first()

		if check is None:
			return 1

		else:
			return 0

class PostRepository():
	def post():
		pass
