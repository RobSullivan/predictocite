# README #

Predictocite uses the title and abstract of an article to predict if it will gain between one and ten citations, or not, in the first two years after publication. 


##Set up a virtualenv

Windows instructions.


##Clone from bitbucket

`git clone https://rsullivan@bitbucket.org/rsullivan/predictocite-flask.git`

##Install

`pip install -r requirements.txt`

##A note on installing scipy and numpy in a virtualenv on Windows

The quickest way found is to add the .exes to the home directory and
run

`easy_install scipy.exe`
`easy_install numpy.exe`

Versions used are scipy==0.14.0 and numpy==1.9.1 (Python3.4)

Installation may be different on other operating systems.


##Data stores
Combination of SQLite and pickles.


##Run tests

cd to home dir
activate virutalevn `Scripts\activate`

run tests
`python manage.py test`


##Start application

In command prompt `python manage.py runserver`

Navigate to localhost:5000

What about db migrations? 

>>>db.create_all()

python manage.py runserver

navigate to localhost://5000

Copyright Birkbeck College, University of London