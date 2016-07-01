from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session
from sqlalchemy_utils import UUIDType
from ..config import *

engine = create_engine(application.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(application)

class User(db.Model):
	__tablename__ = "users"

	id = db.Column('id', UUIDType(binary=False), primary_key=True)
	username = db.Column('username', db.Unicode, unique=True)
	password = db.Column('password', db.Unicode)
	first_name = db.Column('first_name', db.Unicode)
	last_name = db.Column('last_name', db.Unicode)


class Posts(db.Model):
	__tablename__ = "posts"

	id = db.Column('id', UUIDType(binary=False), primary_key=True)
	user_id = db.Column('id', UUIDType(binary=False), db.ForeignKey('users.id'))
	post = db.Column('post', db.Unicode)

	user = db.relationship('User', foreign_keys=user_id)