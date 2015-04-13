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
		#assert_in('PredictoCite',res.body)

	

class TestUserSubmittingData(PredictoCiteTestCase):

	def setUp(self):
		super(TestUserSubmittingData, self).setUp()

	def test_title_abstract_is_submitted_through_form(self):

		res = self.app.get('/')
		form = res.form #get form from its ID
		form['title'] = 'An epigenome paper'
		form['abstract'] = 'A super abstract'
		res = form.submit()
		res.maybe_follow() # redirect after submit form - 302 pattern
		assert_equal(res.status_code, 302)

	def test_submitted_data_displayed_back(self):

		res = self.app.get('/')
		form = res.form #get form from its ID
		form['title'] = 'An epigenome paper'
		form['abstract'] = 'A super abstract'
		res = form.submit()
		res.follow() # redirect after submit form - 302 pattern
		res = self.app.get('/')
		p_text = res.html.find_all(text="An epigenome paper")
		assert_equal('An epigenome paper',p_text.pop())

		

