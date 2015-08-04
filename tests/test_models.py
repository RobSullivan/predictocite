
import unittest
from unittest import mock
from nose.tools import *

from tests.base import PredictoCiteTestCase
from app.models import NbClf, UserDataTransform, YTestData, XTestData

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

	def test_expose_count_vect_and_tf(self):
		self.assertTrue(self.udTransform.count_vect)
		self.assertTrue(self.udTransform.tf_transformer)


class TestY_TestDataIsAvailable(PredictoCiteTestCase):

	def setUp(self):
		super(TestY_TestDataIsAvailable, self).setUp()
		self.y_test = YTestData()

	def test_y_test_data_is_available(self):
		self.assertTrue(self.y_test)

	def test_y_test_has_commensurate_features(self):
		self.assertEqual(len(self.y_test.data), 411)

class TestX_TestDataIsAvailable(PredictoCiteTestCase):

	def setUp(self):
		super(TestX_TestDataIsAvailable, self).setUp()
		self.x_test = XTestData()

	def test_x_test_data_is_available(self):
		self.assertTrue(self.x_test)


