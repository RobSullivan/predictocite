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
		abstract = form.abstract.data
		
		session['title'] = form.title.data
		session['abstract'] = form.abstract.data
		form.title.data = ''
		return redirect(url_for('.index'))
	return render_template('index.html',
	 form=form , title=session.get('title'), abstract=session.get('abstract'))

