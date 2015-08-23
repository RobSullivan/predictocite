from predictocite.datasets.citation_groups import fetch_citationgroups

import numpy as np
from sklearn import cross_validation, metrics
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB




articles = fetch_citationgroups()

#STEP 1: Split data
X_train, X_test, y_train, y_test = cross_validation.train_test_split(
	articles.data, articles.target, test_size=0.25, random_state=25)

#STEP 2: Extract features from text
# tweak params here to see if they return better results.

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


"""
Now carry out cross-validation to evaluate the model

"""

articles_test = count_vect.transform(X_test)

articles_test_tfidf = tf_transformer.transform(articles_test)

predicted = clf.predict(articles_test)

# What's np.mean doing
np.mean(predicted == y_test)









######Grid search
"""
Can't get this working http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html#parameter-tuning-using-grid-search


"""

####Cross-Validation

"""
Can't get this working http://scikit-learn.org/stable/modules/cross_validation.html#computing-cross-validated-metrics

"""

if __name__ == '__main__':
	######Accuracy#########
	print(np.mean(predicted == y_test)*100)

	######Classification report################
	print(metrics.classification_report(y_test, predicted, target_names=y_test))


	#######Confusion matrix#################

	#print(metrics.confusion_matrix(y_test, predicted))
