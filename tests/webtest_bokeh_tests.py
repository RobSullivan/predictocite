"""

Functional tests for data viz using WebTest.

What does the user want to know about the results?

How accurate they are.


"""

import unittest


from nose.tools import *

from tests.base import PredictoCiteTestCase


class TestDisplayAccuracy(PredictoCiteTestCase):

	def setUp(self):
		super(TestActivateViz, self).setUp()


	def test_user_sees_accuracy_of_prediction(self):
		res = self.app.get('/')
		res.form['title'] = 'Lsh mediated RNA polymerase II stalling at HoxC6 and HoxC8 involves DNA methylation.'
		res.form['abstract'] = 'DNA cytosine methylation is an important epigenetic mechanism that is involved in transcriptional silencing of developmental genes. Several molecular pathways have been described that interfere with Pol II initiation, but at individual genes the molecular mechanism of repression remains uncertain. Here, we study the molecular mechanism of transcriptional regulation at Hox genes in dependence of the epigenetic regulator Lsh that controls CpG methylation at selected Hox genes. Wild type cells show a nucleosomal deprived region around the transcriptional start site at methylated Hox genes and mediate gene silencing via Pol II stalling. Hypomethylation in Lsh-/- cells is associated with efficient transcriptional elongation and splicing, in part mediated by the chromodomain protein Chd1. Dynamic modulation of DNA methylation in Lsh-/- and wild type cells demonstrates that catalytically active DNA methyltransferase activity is required for Pol II stalling. Taken together, the data suggests that DNA methylation can be compatible with Pol II binding at selected genes and Pol II stalling can act as alternate mechanism to explain transcriptional silencing associated with DNA methylation.'
		res.form.submit()
		res.maybe_follow()
		res = self.app.get('/result')
		p_text = res.html.find_all('p')
		assert_equal(res.status_code, 200)
		assert_equal("45 percent accurate", p_text[2].text)
