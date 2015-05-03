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
		p_text = res.html.find_all('p')
		assert_equal(res.status_code, 200)
		assert_equal('Title: An epigenome paper',p_text.pop(0).text)

	def test_user_gets_a_prediction(self):

		res = self.app.get('/')
		res.form['title'] = 'Lsh mediated RNA polymerase II stalling at HoxC6 and HoxC8 involves DNA methylation.'
		res.form['abstract'] = 'DNA cytosine methylation is an important epigenetic mechanism that is involved in transcriptional silencing of developmental genes. Several molecular pathways have been described that interfere with Pol II initiation, but at individual genes the molecular mechanism of repression remains uncertain. Here, we study the molecular mechanism of transcriptional regulation at Hox genes in dependence of the epigenetic regulator Lsh that controls CpG methylation at selected Hox genes. Wild type cells show a nucleosomal deprived region around the transcriptional start site at methylated Hox genes and mediate gene silencing via Pol II stalling. Hypomethylation in Lsh-/- cells is associated with efficient transcriptional elongation and splicing, in part mediated by the chromodomain protein Chd1. Dynamic modulation of DNA methylation in Lsh-/- and wild type cells demonstrates that catalytically active DNA methyltransferase activity is required for Pol II stalling. Taken together, the data suggests that DNA methylation can be compatible with Pol II binding at selected genes and Pol II stalling can act as alternate mechanism to explain transcriptional silencing associated with DNA methylation.'
		res.form.submit()
		res.maybe_follow()
		res = self.app.get('/result')
		p_text = res.html.find_all('p')
		assert_equal(res.status_code, 200)
		assert_equal("['one_to_ten_citations']", p_text.pop().text)


class TestUserSavesResult(PredictoCiteTestCase):
	pass


		

