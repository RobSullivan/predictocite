
import unittest
import inspect
from inspect import signature


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
		
		self.assertEqual(form.id, 'titleAbstractForm')

