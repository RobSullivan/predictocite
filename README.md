About
=====
MSc IT project that attempted to predict the number of citations using text analysis.

Installing the application
--------------------------

Here are the steps to install the application on Windows 7/8.

You'll need Python 3.4, which is free to downloaded here: https://www.python.org/downloads/.

It's also a good idea to use a virtual environment with Python so the application's packages
don't conflict with others on the system. This project was developed with Python's virtualenv and 
is easy to use. A good guide for it can be found here: http://docs.python-guide.org/en/latest/dev/virtualenvs/

This application works in Internet Explorer 11, Firefox and Chrome.


Setting up the environment
-----------------------------
Once Python 3.4 is installed and the virtualenv package has been installed follow 
these steps:

1. The application is zipped up as a source distribution file, predictocite-flask-0.0.1.zip, just copy it to a directory and unzip it.
2. Open up a terminal and ``cd`` into predictocite-flask-0.10\\predictocite-flask-0.0.1. This folder will contain the ``setup.py``.
3. Create a virtual environment by entering the command ``virtualenv .``. If Python3.4 is not the main Python interpreter on your machine the -p flag can be used, like so: ``virtualenv . -p /path/to/Python3.4.exe``
4. Activate the virtual environment by typing ``Scripts\\activate``


Installing numpy and scipy
--------------------------

There are numerous issues installing numpy and scipy in virtualenv so both need to be installed before the application. numpy and scipy are packaged with this distribution as .exe files and so can be installed with the ``easy_install``, which will be available as part of the Python virtual environment.

In the terminal:

1. ``easy_install numpy.exe``
2. ``easy_install scipy.exe``

Versions used are numpy1.9.1 and scipy0.14.0.

Installing the application
--------------------------

Now our evnironment is ready to install the application.

In the same directory:

1. ``python setup.py install``
2. ``pip install -r requirements.txt``

Because of the number of dependencies this can take a while to download, unpack and install everything.

With a successful install, read  :doc:`getting_started`.


Errors on install
-----------------

Because of the number of dependencies errors may occur when the install command
downloads and unpacks them. This can be resolved usually by installing them separately with
``pip install <package>``.



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


