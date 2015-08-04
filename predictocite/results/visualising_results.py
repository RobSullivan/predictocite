"""
How-to visualise classification results

Approaches:

Compare features from test doc with features from model.

With poor accuracy how does this work.

Aim: Produce some JSON data for consumption by d3.js 

This uses TfidfVectorizer instead of CountVectorizer and TfidfTransformer

"""

import json

from predictocite.datasets.citation_groups import fetch_citationgroups


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

###User submits data####

user_doc = [X_test[1]]

#vectorized

user_tfidf = tfidf_vect.transform(user_doc)

user_doc_predict = clf.predict(user_tfidf)

#How do I get from user_tfidf matrix to look up features?
# followed this tutorial http://scikit-learn.org/stable/auto_examples/text/document_classification_20newsgroups.html#example-text-document-classification-20newsgroups-py
# uses SelectKBest univariate feature

ch2 = SelectKBest(chi2, k=25)

X_train_tfidf = ch2.fit_transform(X_train_tfidf, y_train)

user_tfidf = ch2.transform(user_tfidf)

#are these top features of user_tfidf or top feautres of X_train_tfidf?
feature_names = [feature_names[i] for i in ch2.get_support(indices=True)]

print(feature_names)

"""
X_test[0]
['cdmrs', 'mapping copy', 'programs human', 'reveals changes', 'targeted bisulfi
te', 'thousands genomes', 'title activates', 'title mapping', 'title seeker', 'v
ariation population']

"""

np.asarray(feature_names)


"""
I need to show why a user_doc has been classified in a particular class.

"""

"""
plotting the confusion matrix

run ipython with --pylab option

Cant plot for one document because user_doc_predict array is dim 1

Show the user the confusion matrix for the test dataset. How does that help

How to deliver the image? load it as an image file

"""

articles_test = tfidf_vect.transform(X_test)

predicted = clf.predict(articles_test)

cm = metrics.confusion_matrix(y_test, predicted)

def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
	plt.imshow(cm, interpolation='nearest', cmap=cmap)
	plt.title(title)
	plt.colorbar()
	tick_marks = np.arange(len(articles.target_names))
	plt.xticks(tick_marks, articles.target_names, rotation=90)
	plt.yticks(tick_marks, articles.target_names)
	plt.tight_layout()
	plt.ylabel('True label')
	plt.xlabel('Predicted label')


plot_confusion_matrix(cm)


"""
cm as json

"""

with open('confusion_matrix.json', 'w') as f:
	json.dump(cm.tolist(), f)


"""
ggplot attempt
"""

data = pd.DataFrame(data=cm, columns=articles.target_names, fill=np.arange(len(articles.target_names)))

ggplot(data, aes(x=articles.target_names, y=articles.target_names)) +\
	scale_color_gradient(low='blue', mid='white', high='red') +\
	geom_tile(aes(fill='#333333'))

#KeyError: 'fill' - known bug - fix has not fixed it by the look of it.


"""
Bokeh attempt - works the best so far as outputs html.

Get some colour mapping on this.

Figure out how to call and render this from results page.

"""
from bokeh.charts import HeatMap, output_file, show

output_file('heatmap.html')

p = HeatMap(cm, title='Confusion Matrix')

show(p)