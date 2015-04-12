'''Functional tests using WebTest'''

import unittest


from nose.tools import *

from tests.base import PredictoCiteTestCase

class TestNavigateToIndex(PredictoCiteTestCase):

	def setUp(self):
		super(TestNavigateToIndex, self).setUp()


	def test_navigate_to_index(self):
		"""User gets index page"""
		res = self.app.get('/')
		assert_equal(res.status, '200 OK')

	

class TestUserSubmittingData(PredictoCiteTestCase):

	def setUp(self):
		super(TestUserSubmittingData, self).setUp()

	def test_title_abstract_is_submitted_through_form(self):

		res = self.app.get('/')
		form = res.forms #get form from its ID
		form.submit()
		assert_true(form)
		

