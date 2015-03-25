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
	   


	"""

	def __init__(self, articles):
		self.articles = articles
		self.count_vect = CountVectorizer(max_df=1, stop_words='english', ngram_range=(1, 2))
		self.tf_transformer = TfidfTransformer(norm='l2')

	def split_data(self):
		split_datasets = {}
		SPLIT_PERC = 0.75
		split_size = int(len(self.articles.data)*SPLIT_PERC)
		split_datasets['train'] = self.articles.data[:split_size]
		split_datasets['test'] = self.articles.data[split_size:]
		return split_datasets

	def bag_of_words(self):
		"""Transforms into a vector, probably should rename from bag_of_words"""
		training_data = self.split_data()
		term_freq_vectors = self.count_vect.fit_transform(training_data['train']) # this changes state of self.count_vect
		return term_freq_vectors 

	def frequency_term_matrix(self, data):
		"""takes train set and returns frequency_term matrix"""
		self.count_vect.fit_transform(data);
		sparse_matrix = self.count_vect.transform(data)
		


		return sparse_matrix.todense()
		

	def tfidf_fit_transform(self, freq_term_matrix):
				
		tfidf = self.tf_transformer.fit(freq_term_matrix)#fit_transform creates a vocbulary index
		return tfidf
		

	def save_pickle(self, groups, tf_idf_matrix):
		file_name = 'tf_idf_matrix'+groups[0]+'.pickle'
		try:
			with open(file_name, 'wb') as f:
				pickle.dump(tf_idf_matrix, f, pickle.HIGHEST_PROTOCOL)
		except Exception, e:
			raise
			
		





if __name__ == '__main__':
	unittest.main()
