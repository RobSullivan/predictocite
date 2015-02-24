import unittest

from predictocite.datasets.citation_groups import fetch_citationgroups


class TestCitationDataAttributes(unittest.TestCase):
	"""TestCitationDataAttributes tests that data is retrieved with attributes necessary for 
	processing"""
	
	def setUp(self):
		groups = ['one_to_ten_citations', 'eleven_to_twenty_citations']
		self.articles = fetch_citationgroups(groups)

	def test_fetch_citationgroups(self):
		citation_group = 'one_to_ten_citations'
		self.assertTrue(citation_group in self.articles.target_names)
		self.assertTrue(citation_group in self.articles.target)
		self.assertEqual(len(self.articles.data), len(self.articles.target))





if __name__ == '__main__':
	unittest.main()
