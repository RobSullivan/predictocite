import unittest

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
	vectorizer and classifier will be TfidVectorizer and MultinomialNB
	as these give best performance in the book. Eventually try other vectorizers
	and other classifiers for comparison.
	

	params
	-------
	vect - TfidfVectorizer
	clf - Classifier, the MultinomialNB class
	"""
	
