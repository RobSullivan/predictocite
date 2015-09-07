Running the application
====================================

Running the tests
-----------------

To check everything is working as intended, run the tests.

1. ``python manage.py test``

This runs *all* the tests.

To run individual tests Python's *nose* test tool can be used.

2. ``nosetests tests\\test_webtest_tests.py``


Starting the application
------------------------

1. ``python mangage.py runserver``
2. open a web browser and navigate to http://localhost:5000/


Enter some test data
--------------------

Here's some test data from a highly cited `article <http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0009163>`_ to copy and paste into the application.



**Title**: Lsh mediated RNA polymerase II stalling at HoxC6 and HoxC8 involves DNA methylation.

**Abstract**: DNA cytosine methylation is an important epigenetic mechanism that is involved in transcriptional silencing of developmental genes. Several molecular pathways have been described that interfere with Pol II initiation, but at individual genes the molecular mechanism of repression remains uncertain. Here, we study the molecular mechanism of transcriptional regulation at Hox genes in dependence of the epigenetic regulator Lsh that controls CpG methylation at selected Hox genes. Wild type cells show a nucleosomal deprived region around the transcriptional start site at methylated Hox genes and mediate gene silencing via Pol II stalling. Hypomethylation in Lsh-/- cells is associated with efficient transcriptional elongation and splicing, in part mediated by the chromodomain protein Chd1. Dynamic modulation of DNA methylation in Lsh-/- and wild type cells demonstrates that catalytically active DNA methyltransferase activity is required for Pol II stalling. Taken together, the data suggests that DNA methylation can be compatible with Pol II binding at selected genes and Pol II stalling can act as alternate mechanism to explain transcriptional silencing associated with DNA methylation.

Press submit to get the prediction!