from ..repository.repository import *
from passlib.hash import bcrypt

## Service layer does most of the logic for your API and offloads any database transaction to the repository layer.
class User():
	def Authtoken(username, password):
		exsist = UserRepository.does_exsist(username)

		if exsist == 1:
			return 0

		else:


	def Signup():
		pass

class Post():
	def Post():
		pass

