from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required

class NameForm(Form):
	name = StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')

class TitleAbstractForm(Form):
	title = StringField(validators=[Required()])
	abstract = TextAreaField(validators=[Required()])
	submit = SubmitField('Submit')