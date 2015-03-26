import unittest

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from predictocite.classifiers.build_classifier import BuildClassifier


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

	def test_create_pipeline(self):

		pipeline = Pipeline(self.steps)
		build_clf = BuildClassifier(self.steps)
		
		self.assertIsInstance(build_clf.pipeline, Pipeline)
	
