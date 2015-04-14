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
		form = res.form 
		form['title'] = 'An epigenome paper'
		form['abstract'] = 'A super abstract'
		res = form.submit()
		res.maybe_follow() # redirect after submit form - 302 pattern
		res = self.app.get('/')
		p_text = res.html.find_all(text="An epigenome paper")
		assert_not_equal('An epigenome paper', p_text)

	def test_user_data_displayed_on_result_page(self):

		res = self.app.get('/')
		form = res.form 
		form['title'] = 'An epigenome paper'
		form['abstract'] = 'A super abstract'
		res = form.submit()
		res.maybe_follow() # redirect after submit form - 302 pattern
		res = self.app.get('/result')
		p_text = res.html.find_all(text="An epigenome paper")
		assert_equal(res.status_code, 200)
		assert_equal('An epigenome paper',p_text.pop())

	def test_user_gets_a_prediction(self):

		res = self.app.get('/')
		res.form['title'] = ''
		res.form['abstract'] = ''
		res.form.submit()
		res.maybe_follow()
		res = self.app.get('/result')
		p_text = res.html.find_all(text="one_to_ten_citations")
		assert_equal(res.status_code, 200)
		assert_equal('one_to_ten_citations', p_text)


class TestUserSavesResult(PredictoCiteTestCase):
	pass


		

