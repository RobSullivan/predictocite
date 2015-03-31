

from sklearn.pipeline import Pipeline


class BuildClassifier():
	"""
Code inspired by https://www.safaribooksonline.com/library/view/
learning-scikit-learn-machine/9781783281930/ch02s02.html

Builds a classifier using Pipeline and then evaulates and trains
classifier

evaluate and perform needs to use all the article data.

Remember to check where the shuffling occurs and if the articles.target
attribute is a problem not a numpy array

Parameters
-------
steps: a list of tuples comprised of a vectorizer 'vect' and a classifier 'clf'
       For example the vectorizer TfidfVectorizer and the classifier MultinomialNB.

articles: a type Bunch of article data
"""
	def __init__(self, steps, articles=None):
		self.steps = steps
		self.articles = articles
		self.pipeline = Pipeline(steps)

	def evaluate_cross_validation(self):
		pass



if __name__ == '__main__':
	unittest.main() #er, what does unittest.main() mean? where did it come from?