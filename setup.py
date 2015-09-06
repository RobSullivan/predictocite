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
	})