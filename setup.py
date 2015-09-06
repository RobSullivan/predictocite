from setuptools import setup, find_packages

setup(
	name='predictocite-flask',
	version='0.1.0',
	description='MSc IT project implementation',
	long_description='Project for MSc IT. A web application \
	to predict number of citations given a title and abstract',
	author='Robert Sullivan',
	author_email='robertjsullivan.esq@gmail.com',
	url='https://bitbucket.org/rsullivan/predictocite-flask',
	license='Birkbeck',
	classifiers=[

	'Development Status :: 3 - Alpha',

	'Intended Audience :: STM Editors',
	'Topic :: Text Analysis, Classification',

	'Licence :: Birkbeck',

	'Programming Language :: Python :: 3.4'
	
	],
	keywords='classification text analysis flask',
	packages=['app', 'predictocite', 'tests'],
	include_package_data=True,
	package_data={
	'data':'predictocite-flask\\data\\*',
	'templates':'predictocate-flask\\app\\templates\\*',
	},
	test_suite = 'predictocite-flask.tests'	
	,
	entry_points={
	'console_scripts':[
	'runserver = manage']
	},install_requires=['Babel==2.0',
'Flask==0.10.1',
'Flask-Bootstrap==3.3.0.1',
'Flask-Migrate==1.3.0',
'Flask-SQLAlchemy==2.0',
'Flask-Script==2.0.5',
'Flask-WTF==0.11',
'Jinja2==2.7.3',
'Mako==1.0.1',
'Markdown==2.6.2',
'MarkupSafe==0.23',
'PyYAML==3.11',
'Pygments==2.0.2',
'SQLAlchemy==0.9.8',
'Sphinx==1.3',
'WTForms==2.0.2',
'WebOb==1.4',
'WebTest==2.0.18',
'Werkzeug==0.10.1',
'alabaster==0.7.6',
'alembic==0.7.4',
'beautifulsoup4==4.3.2',
'bokeh==0.9.2',
'brewer2mpl==1.4.1',
'certifi==2015.04.28',
'colorama==0.3.3',
'coverage==3.7.1',
'docutils==0.12',
'ggplot==0.6.5',
'greenlet==0.4.7',
'husl==4.0.2',
'itsdangerous==0.24',
'matplotlib==1.4.3',
'nose==1.3.4',
'patsy==0.3.0',
'pkginfo==1.2.1',
'pymongo==2.7.2',
'pyparsing==2.0.3',
'pystache==0.5.4',
'python-dateutil==2.4.2',
'pytz==2015.4',
'requests==2.7.0',
'scikit-learn==0.15.2',
'six==1.9.0',
'snowballstemmer==1.2.0',
'sphinx-rtd-theme==0.1.8',
'statsmodels==0.6.1',
'sympy==0.7.6',
'tornado==4.1',
'twine==1.5.0',
'waitress==0.8.9',
'wheel==0.24.0',
])