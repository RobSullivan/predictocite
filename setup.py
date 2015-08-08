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
	packages=find_packages(),
	include_package_data=True,
	data_files=[''],# list pickles and sqlite db,
	install_requires=[])