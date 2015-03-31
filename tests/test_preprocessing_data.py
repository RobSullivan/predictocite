import unittest

from nose.tools import nottest


from predictocite.datasets.citation_groups import fetch_citationgroups
from predictocite.datasets.preprocessing import TextPreprocessor

class TestPreprocessingOfData(unittest.TestCase):
	"""
	TestPreprocessingOfData tests turning text into numbers
	"""
	def setUp(self):
		self.groups = ['one_to_ten_citations']
		self.articles = fetch_citationgroups(self.groups)
		preprocessor = TextPreprocessor(self.articles)
		split_data = preprocessor.split_data()

	

	@unittest.skip
	def test_write_tfidf_to_pickle(self):
		"""
		STILL TO IMPLEMENT
		For convenience of not using a datastore, write tfidf_matrix 
		out to a pickle.
		"""
		preprocessor.save_pickle(tfidf_matrix)
		
		

	def test_preprocessing_bag_of_words(self):
		"""
		bag_of_words will return a scipy.frequency_term.csr.csr_matrix so test for these attrs.
		
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

	def test_create_frequency_term_matrix(self):
		"""
		Once have vocab indexed create frequency_term matrix 
		"""
		preprocessor = TextPreprocessor(self.articles)
		split_data = preprocessor.split_data()
		preprocessor.count_vect.fit_transform(split_data['train'])
		frequency_term_matrix = preprocessor.frequency_term_matrix(split_data['train']) #preprocessor.count_vect.transform(split_data['train'])
		
		self.assertTrue(hasattr(frequency_term_matrix, 'transpose'))

	def test_term_frequency_features(self):
		"""
		tf-idf helper test
		The last step before classification
		"""
		#tfidf_transformer = TfidfTransformer()
		preprocessor = TextPreprocessor(self.articles)
		split_data = preprocessor.split_data()
		
		term_freq_matrix = preprocessor.frequency_term_matrix(split_data['train'])
		
		tfidf = preprocessor.tf_transformer.fit(term_freq_matrix)
		self.assertEqual(tfidf.norm, 'l2')


	
	def test_tfidf_weighting(self):
		preprocessor = TextPreprocessor(self.articles)
		split_data = preprocessor.split_data()
		term_freq_matrix = preprocessor.frequency_term_matrix(split_data['train'])

		
		preprocessor.tf_transformer.fit(term_freq_matrix)
		
		self.assertTrue(preprocessor.tf_transformer, 'idf_')

