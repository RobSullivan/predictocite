import pickle

from sklearn import cross_validation
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB


from predictocite.datasets.citation_groups import fetch_citationgroups


articles = fetch_citationgroups()

#STEP 1: Split data
X_train, X_test, y_train, y_test = cross_validation.train_test_split(
	articles.data, articles.target, test_size=0.25, random_state=25)

#STEP 2: Extract features from text

count_vect = CountVectorizer(max_df=1, stop_words='english', ngram_range=(1, 2))

"""
fit_transform learns the vocabulary dictionary
and return term-document matrix

"""
X_train_counts = count_vect.fit_transform(X_train)

# then go from occurences to frequencies

tf_transformer = TfidfTransformer(norm='l2')

X_train_tfidf = tf_transformer.fit_transform(X_train_counts)

#STEP 3: train a classifer 

clf = MultinomialNB().fit(X_train_tfidf, y_train)

#STEP 4: predict new doc
user_doc = [X_test[0]] # new doc for classifying needs to be in a list

"""
To predict the outcome on a new document we need to extract the features using
almost the same feature extracting chain as before. The difference is that
we call transform instead of fit_transform on the transformers, since they have
already been to fit to the training set 
"""

X_new_counts = count_vect.transform(user_doc)

X_new_tfidf = tf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

