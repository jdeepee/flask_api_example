from flask import Flask
from flask_restful import Resource, Api 

application = Flask(__name__) #Creating application
api = Api(application) #Creating API

#Import our database model
from database.database_model import *

db.init_app(application)
Session = sessionmaker()
Session.configure(bind=engine)

#Initialise the database session
session = Session()
session._model_changes = {}

#Importing our classes
from rest.routes import index
from rest.routes import post
from rest.routes import users

## Mapping our resource classes to routes

#Index
api.add_resource(index, '/')

#Users
api.add_resource(User, '/users/')
api.add_resource(UserGet, '/users/<id>/') #<ID> will allow us to handle URL extensions, id can then be passed to appropriate function and used.
api.add_resource(AuthToken, '/authtoken/')

#Posts
api.add_resource(PostContent, '/post/')
api.add_resource(PostContent, '/post/<id>')