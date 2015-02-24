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

	def test_user_knows_they_are_at_predictocite(self):

		res = self.app.get('/').maybe_follow()


class TestUserCanSubmitData(PredictoCiteTestCase):

	pass:
