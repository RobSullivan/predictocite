"""
How-to visualise classification results

Approaches:

Compare features from test doc with features from model.

With poor accuracy how does this work.

Aim: Produce some JSON data for consumption by d3.js 

This uses TfidfVectorizer instead of CountVectorizer and TfidfTransformer

"""

from predictocite.datasets.citation_groups import fetch_citationgroups

import numpy as np
from sklearn import cross_validation, metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB




articles = fetch_citationgroups()

#STEP 1: Split data
X_train, X_test, y_train, y_test = cross_validation.train_test_split(
	articles.data, articles.target, test_size=0.25, random_state=25)

#STEP 2: Extract features from text using TfidfVectorizer

tfidf_vect = TfidfVectorizer(max_df=1, stop_words='english', ngram_range=(1, 2), encoding='utf-8')

"""
fit_transform learns the vocabulary dictionary
and return term-document matrix

"""

X_train_tfidf = tfidf_vect.fit_transform(X_train)
trained_features = tfidf_vect.get_feature_names() #a list

#STEP 3: train a classifer 

clf = MultinomialNB().fit(X_train_tfidf, y_train)

###User submits data####

user_doc = [X_test[0]]

#vectorized

user_tfidf = tfidf_vect.transform(user_doc)

#How do I get from user_tfidf matrix to look up features?





