from flask import render_template, session, redirect, url_for
from . import main
from .forms import TitleAbstractForm
from .. import db
from ..models import User, NbClf, UserDataTransform, YTestData

import numpy as np

@main.route('/', methods=['GET', 'POST'])
def index():
	
	form = TitleAbstractForm()


	if form.validate_on_submit():
		data_transform = UserDataTransform()
		nb_clf = NbClf()
		title = form.title.data
		abstract = form.abstract.data
		
		session['nb_clf'] = nb_clf

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
	y_test_data = y_test.data

	nb_clf = session.get('nb_clf')

	#predicted = nb_clf.clf.predict(y_test_data)

	#accuracy  = np.mean(predicted == y_test_data)



	return render_template('result.html', 
		title=session.get('title'), user_data=session.get('user_data'), 
		abstract=session.get('abstract'), prediction=session.get('prediction'),
		accuracy=nb_clf)