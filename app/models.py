import pickle
import sys

from . import db



class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	users = db.relationship('User', backref='role', lazy='dynamic')

	def __repr__(self):
		return '<Role %r>' % self.name

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
	def __repr__(self):
		return '<User %r>' % self.username


class NbClf():
	"""NbClf loads and wraps clf.pickle"""
	def __init__(self):
		try:
			with open('nb_classifier.pickle', 'rb') as f:
				self.clf = pickle.load(f)
		except IOError as err:
			print("IO Error: {0}".format(err))


class UserDataTransform():
	"""loads and wraps count_vect and tf_transform
	that generated clf.pickle. Use them to transform 
	user's title and abstract into a frequency matrix"""
	def __init__(self):
		try:
			with open('count_vect.pickle', 'rb') as f:
				self.count_vect = pickle.load(f)
		except IOError as err:
			print("IO Error: {0}".format(err))
		try:
			with open('tf_transformer.pickle', 'rb') as g:
				self.tf_transformer = pickle.load(g)
		except IOError as err:
			print("IO Error: {0}".format(err))


class YTestData(object):
	"""YTestData loads y_test pickle
	   This is needed for accuracy score and 
	   confusion matrix.

	   Current way to load is to do it on __init__
	   so the object becomes the depickled pickle 
	   and is available to use straight away.
	"""
	def __init__(self):
		with open('y_test.pickle', 'rb') as f:
			self.data = pickle.load(f)


class XTestData(object):
	"""XTestData loads X_test pickle
	   This is needed for accuracy score and 
	   confusion matrix.

	   Current way to load is to do it on __init__
	   so the object becomes the depickled pickle 
	   and is available to use straight away.
	"""
	def __init__(self):
		with open('X_test.pickle', 'rb') as f:
			self.data = pickle.load(f)