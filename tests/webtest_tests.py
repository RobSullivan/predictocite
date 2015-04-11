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

	

class TestSubmittingData(PredictoCiteTestCase):

	def setUp(self):
		super(TestSubmittingData, self).setUp()

	def test_can_enter_title_into_form(self):

		res = self.app.get('/')
		form = res.forms['title_abstract_form'] #get form from its ID
		assert_true(form)

