"""
How-to visualise classification results with Bokeh

With poor accuracy how does this work.

This uses TfidfVectorizer instead of CountVectorizer and TfidfTransformer

"""

import json

from predictocite.datasets.citation_groups import fetch_citationgroups


from bokeh.charts import HeatMap, output_file, show
import numpy as np
import pandas as pd
from sklearn import cross_validation, metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.naive_bayes import MultinomialNB




articles = fetch_citationgroups()

#STEP 1: Split data
X_train, X_test, y_train, y_test = cross_validation.train_test_split(
	articles.data, articles.target, test_size=0.25, random_state=25)

#STEP 2: Extract features from text using TfidfVectorizer

tfidf_vect = TfidfVectorizer(max_df=1, stop_words='english', ngram_range=(1, 2), encoding='utf-8', max_features=50000)

"""
fit_transform learns the vocabulary dictionary
and return term-document matrix

"""

X_train_tfidf = tfidf_vect.fit_transform(X_train)
feature_names = tfidf_vect.get_feature_names() #a list

#STEP 3: train a classifer 

clf = MultinomialNB().fit(X_train_tfidf, y_train)




"""
I need to show why a user_doc has been classified in a particular class.

"""


articles_test = tfidf_vect.transform(X_test)

predicted = clf.predict(articles_test)

cm = metrics.confusion_matrix(y_test, predicted)

plot_confusion_matrix(cm)




output_file('heatmap.html')

p = HeatMap(cm, title='Confusion Matrix')

show(p)

"""
Test how to embed this plot into the results page.
"""

from bokeh.plotting import figure
from bokeh.embed import components

plot = figure()
plot.circle([1,2], [3,4])

script, div = components(plot)


"""
How to This lets us nicely see the relationship between predicted and actual classes.
The axis show the log probability
colour to identify the actual class for items and draw a line to represent the decision boundary 


predicted vs y_test


"""
