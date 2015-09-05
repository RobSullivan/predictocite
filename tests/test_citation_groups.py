import unittest

from predictocite.datasets.citation_groups import fetch_citationgroups


class TestCitationDataAttributes(unittest.TestCase):
	"""TestCitationDataAttributes tests that data is retrieved with attributes necessary for 
	processing"""
	
	def setUp(self):
		groups = ['zero_citations', 'one_to_five_citations']
		self.articles = fetch_citationgroups(groups)
	
	

	def test_fetch_citationgroups(self):
		citation_group = 'one_to_five_citations'
		self.assertTrue(citation_group in self.articles.target_names)
		self.assertTrue(citation_group in self.articles.target)
		self.assertEqual(len(self.articles.data), len(self.articles.target))

	def test_fetch_all_citationgroups(self):
		self.all_articles = fetch_citationgroups() 
		self.assertTrue(self.all_articles)







if __name__ == '__main__':
	unittest.main()
