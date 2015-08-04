
import unittest



from nose.tools import *

from app.main import views
from tests.base import PredictoCiteTestCase
from app.main.forms import NameForm

class TestIndexView(PredictoCiteTestCase):

	def setUp(self):
		super(TestIndexView, self).setUp()

		

	def test_index_has_title_and_abstract_form(self):
		res = self.app.get('/')
		form = res.form
		fields = form.fields
		self.assertIn('title', fields)
		self.assertIn('abstract', fields)
		self.assertIn('submit', fields)

	def test_result_page_exists(self):
		res = self.app.get('/result')
		self.assertEqual(res.status_code, 200)




class TestResultView(PredictoCiteTestCase):

	def setUp(self):
		super(TestResultView, self).setUp()

	def test_result_template_has_space_for_accuracy_score(self):
		res = self.app.get('/result')
		p = res.html.find_all('p')
		self.assertEqual(len(p), 4)

	def test_result_view_calculates_accuracy(self):
		res = self.app.get('/result')
		self.assertEqual(res.status_code, 200)





