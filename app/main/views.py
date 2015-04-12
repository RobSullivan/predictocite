from flask import render_template, session, redirect, url_for
from . import main
from .forms import TitleAbstractForm
from .. import db
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
	
	form = TitleAbstractForm()
	if form.validate_on_submit():
		title = form.title.data
		#if user is None:
		#	user = User(username=form.name.data)
		#	db.session.add(user)
		#	db.session.commit()
		#	session['known'] = False
		#else:
		#	session['known'] = True
		session['title'] = form.title.data
		#form.name.data = ''
		return redirect(url_for('.index'))
	return render_template('index.html',
	 form=form, title=session.get('title'))

