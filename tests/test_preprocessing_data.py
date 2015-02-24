import unittest



from predictocite.datasets.citation_groups import fetch_citationgroups
from predictocite.datasets.preprocessing import TextPreprocessor

class TestPreprocessingOfData(unittest.TestCase):
	"""
	TestPreprocessingOfData tests turning text into numbers
	"""
	def setUp(self):
		groups = ['one_to_ten_citations']
		self.articles = fetch_citationgroups(groups)
		
		

	def test_preprocessing_bag_of_words(self):
		"""
		bag_of_words will return a scipy.sparse.csr.csr_matrix so test for these attrs.
		
		"""
		
		preprocessor = TextPreprocessor(self.articles)
		x_train_counts = preprocessor.bag_of_words()
		self.assertTrue(hasattr(x_train_counts, 'shape'))


	def test_split_data_for_training_and_testing(self):
		"""
		training_data will be 75 percent len of data
		test_data will be 25 percent len of data
		len of groups is 965
		"""

		preprocessor = TextPreprocessor(self.articles)
		split_data = preprocessor.split_data()
		self.assertEqual(len(split_data['train']), 723)
		self.assertEqual(len(split_data['test']), 242)

	def test_term_frequency_features(self):
		"""
		tf-idf helper after bag_of_words.
		The last step before classification
		"""
		#tfidf_transformer = TfidfTransformer()
		preprocessor = TextPreprocessor(self.articles)
		#data = preprocessor.split_data()
		X_train_tfidf = preprocessor.tfidf_fit_transform()# is a helper method for tfidf_transformer.fit_transform()
		self.assertTrue(hasattr(X_train_tfidf, 'shape'))
