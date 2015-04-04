import unittest

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from predictocite.classifiers.build_classifier import BuildClassifier
from predictocite.datasets.citation_groups import fetch_citationgroups


class TestBuildClassifier(unittest.TestCase):
	"""
	TestBuildClassifier - aim is to build a classifer that 
	returns a model ready for evaluating its performance

	BuildClassifier class needs to do the following:
	- build a classifier
	- be able to be trained in entire training set 
	- be evaluated in the training set
	- be evaluated in the test set 
	- be pickled with its state saved
	- accept a vectorizer and a classifier

	For reference see ch02 of 'Learning scikit-learn:Machine Learning in
	Python.
	vectorizer and classifier will be TfidfVectorizer and MultinomialNB
	as these give best performance in the book. Eventually try other vectorizers
	and other classifiers for comparison.
	

	params
	-------
	vect - TfidfVectorizer
	clf - Classifier, the MultinomialNB class
	"""
	def setUp(self):
		
		self.vect = TfidfVectorizer()
		self.clf = MultinomialNB()
		self.steps = [('vect', self.vect),
		('clf', self.clf)]# list of tuples
		self.articles = fetch_citationgroups()


	def tearDown(self):
		self.vect = None
		self.clf = None
		self.steps = None
		self.articles = None

	def test_create_pipeline(self):

		pipeline = Pipeline(self.steps)
		build_clf = BuildClassifier(self.steps)
		
		self.assertIsInstance(build_clf.pipeline, Pipeline)

	def test_build_classifier_has_evaluate_cross_validation_method(self):

		build_clf = BuildClassifier(self.steps)
		self.assertTrue(hasattr(build_clf, 'evaluate_cross_validation'))

	def test_build_classifier_has_all_the_data(self):
		build_clf = BuildClassifier(self.steps, self.articles)
		self.assertGreater(len(build_clf.articles['data']), 1000)#len = 1644

	def test_evaluate_method_returns_array_of_scores(self):


		build_clf = BuildClassifier(self.steps, self.articles)
		
		scores = build_clf.evaluate_cross_validation()
		self.assertTrue(hasattr(scores, 'shape'))

	
