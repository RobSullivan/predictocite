"""

Text preprocessing helper functions.

"""

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer


class TextPreprocessor:
	"""TextPreprocessor takes text data and provides methods for turning
	   text into feature vectors using skearn.
	   It splits data into train and test on __init__ and stores as self.train & self.test
	   Heavily based on http://scikit-learn.sourceforge.net/stable/tutorial/text_analytics/
	   working_with_text_data.html#extracting-features-from-text-files
	   
	   Parameters

	   -----

	   articles: document data for citation groups represented as a list.
	   has the following attributes in addition to usual list attrs:
	   data - list of documents as str objects
	   citation_count - number of citations per document (two years after publication)
	   obect_ids - MongoDb Id 
	   target - label
	   target_names - list of all labels


	"""

	def __init__(self, articles):
		self.articles = articles
		self.count_vect = CountVectorizer(max_df=1, stop_words='english')
		self.tf_transformer = TfidfTransformer()

	def split_data(self):
		split_datasets = {}
		SPLIT_PERC = 0.75
		split_size = int(len(self.articles.data)*SPLIT_PERC)
		split_datasets['train'] = self.articles.data[:split_size]
		split_datasets['test'] = self.articles.data[split_size:]
		return split_datasets

	def bag_of_words(self):

		training_data = self.split_data()
		X_train_counts = self.count_vect.fit_transform(training_data['train']) # this changes state of self.count_vect
		return X_train_counts 

	def tfidf_fit_transform(self):
		X_train_counts = self.bag_of_words()
		
		X_train_tf = self.tf_transformer.fit_transform(X_train_counts)#fit_transform creates a vocbulary index
		return X_train_tf
		






if __name__ == '__main__':
	unittest.main()
