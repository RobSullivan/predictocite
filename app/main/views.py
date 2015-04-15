from flask import render_template, session, redirect, url_for
from . import main
from .forms import TitleAbstractForm
from .. import db
from ..models import User, NbClf, UserDataTransform

@main.route('/', methods=['GET', 'POST'])
def index():
	
	form = TitleAbstractForm()


	if form.validate_on_submit():
		data_transform = UserDataTransform()
		nb_clf = NbClf()
		title = form.title.data
		abstract = form.abstract.data
		
		session['title'] = form.title.data
		session['abstract'] = form.abstract.data
		user_data = [title + ' ' + abstract]
		session['user_data'] = user_data
		user_data_bag_of_words = data_transform.count_vect.transform(user_data)
		frequency_matrix = data_transform.tf_transformer.transform(user_data_bag_of_words)
		prediction = nb_clf.clf.predict(frequency_matrix)
		session['prediction'] = prediction
		

		form.title.data = ''
		return redirect(url_for('.result'))
	return render_template('index.html',
	 form=form)


@main.route('/result', methods=['GET'])
def result():
	return render_template('result.html', 
		title=session.get('title'), user_data=session.get('user_data'), 
		abstract=session.get('abstract'), prediction=session.get('prediction'))