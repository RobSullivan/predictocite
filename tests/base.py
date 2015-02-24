

'''Functional tests using WebTest'''
import unittest

from flask import current_app
from nose.tools import *
from webtest import TestApp

from app import create_app, db



class AppTestCase(unittest.TestCase):
	'''Base `TestCase` for predictocite tests that require WSGI app and db'''

	def setUp(self):
		super(AppTestCase, self).setUp()
		self.test_app = create_app('testing')
		self.app = TestApp(self.test_app)
		self.context = self.test_app.app_context()
		self.context.push()
		

	def tearDown(self):
		super(AppTestCase, self).tearDown()
		self.context.pop()


class DbTestCase(unittest.TestCase):
	pass


class PredictoCiteTestCase(AppTestCase):
	"""Base `TestCase` for tests that require both databases
	and the predictocite application. Superclass call `super` in order
	for all setup and teardown methods to be called correctly"""
	pass


