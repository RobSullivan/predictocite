

from sklearn.pipeline import Pipeline


class BuildClassifier(Pipeline):
	"""
Code inspired by https://www.safaribooksonline.com/library/view/
learning-scikit-learn-machine/9781783281930/ch02s02.html

Builds a classifier using Pipeline and then evaulates and trains
classifier

Uses all the article data.

Remember to check where the shuffling occurs and if the articles.target
attribute is a problem not a numpy array

docstring for TestBuildClassifier
	build_classifier will use Pipeline class from sklearn which 
	accepts a vectorizer and a Bayes classifier.
	As per ch02 of 'Learning scikit-learn:Machine Learning in
	Python I have used the MultinomialNB class.
	Will also use the TfidfVectorizer
	TfidfTransformer
	

	params (or steps for Pipeline)
	-------
	vect - TfidfVectorizer
	clf - Classifier, the MultinomialNB class

"""
	pass




if __name__ == '__main__':
	unittest.main() #er, what does unittest.main() mean? where did it come from?