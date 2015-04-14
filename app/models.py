import pickle

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
		with open('clf.pickle', 'rb') as f:
			self.clf = pickle.load(f)


class UserDataTransform():
	pass

"""
class NbClassifier(db.Model):
	
	This class loads clf.pickle as a clf property
	clf property then has the clf API available
	a view function can then use this class 
	to submit user data to
	
	pass


class TransformUserData(db.Model):

	returns a frequency matrix from user data

	pass
"""