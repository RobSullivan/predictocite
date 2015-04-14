
import unittest
from unittest import mock
from nose.tools import *

from tests.base import PredictoCiteTestCase
from app.models import NbClf, UserDataTransform
class TestClassiferModel(PredictoCiteTestCase):

	def setUp(self):
		super(TestClassiferModel, self).setUp()
		self.nb_clf = NbClf()

	def test_nbclf_model_exists(self):

		self.assertTrue(self.nb_clf)

	def test_pickle_loaded_on_init(self):

		self.assertTrue(self.nb_clf.clf)

	def test_clf_obj_has_expected_api(self):
		clf = self.nb_clf.clf
		self.assertTrue(hasattr(clf, 'predict'))


class TestUserDataTransformModel(PredictoCiteTestCase):

	def setUp(self):
		super(TestUserDataTransformModel, self).setUp()
		self.udTransform = UserDataTransform()

	def test_tfidf_model_exists(self):
		self.assertTrue(self.udTransform)


