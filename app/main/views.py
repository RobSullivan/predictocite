from flask import render_template, session, redirect, url_for, Markup
from . import main
from .forms import TitleAbstractForm
from .. import db
from ..models import User, NbClf, UserDataTransform, YTestData, XTestData

import numpy as np

@main.route('/', methods=['GET', 'POST'])
def index():
	
	form = TitleAbstractForm()


	if form.validate_on_submit():
		data_transform = UserDataTransform()
		nb_clf = NbClf()
		title = form.title.data
		abstract = form.abstract.data
		
		# add classifier and vectorizers to session so result route can 
		# pick them up

		#session['nb_clf'] = nb_clf
		#session['data_transform'] = data_transform

		session['title'] = form.title.data
		session['abstract'] = form.abstract.data
		user_data = [title + ' ' + abstract]
		session['user_data'] = user_data
		user_data_bag_of_words = data_transform.count_vect.transform(user_data)
		frequency_matrix = data_transform.tf_transformer.transform(user_data_bag_of_words)
		prediction = nb_clf.clf.predict(frequency_matrix)
		session['prediction'] = str(prediction)
		


		form.title.data = ''
		return redirect(url_for('.result'))
	return render_template('index.html',
	 form=form)


@main.route('/result', methods=['GET'])
def result():

	y_test = YTestData()
	x_test = XTestData()

	y_test_data = y_test.data
	x_test_data = x_test.data

	# if going via index first could use session.get('nb_clf')
	# but looks like might have to violate DRY when hitting result directly
	# this needs refactoring at some point
	nb_clf = NbClf()
	data_transform = UserDataTransform()

	#count_vect x_test_data
	articles_test = data_transform.count_vect.transform(x_test_data)

	#this is tfidf...
	articles_test = data_transform.tf_transformer.transform(articles_test)

	predicted = nb_clf.clf.predict(articles_test)

	accuracy  = round(np.mean(predicted == y_test_data)*100, 2)

	plot_div = Markup('<div class="plotdiv"></div>')
	plot_script = Markup('<script></script>')


	return render_template('result.html', 
		title=session.get('title'), user_data=session.get('user_data'), 
		abstract=session.get('abstract'), prediction=session.get('prediction'),
		accuracy=accuracy, plot_div=plot_div, plot_script=plot_script)