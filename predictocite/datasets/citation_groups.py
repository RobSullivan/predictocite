"""Loader for the citation groups from mongodb pcite database

modelled on https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/twenty_newsgroups.py#L151

sqlite3 code from https://docs.python.org/3.4/library/sqlite3.html

This dataset loader will retrieve title and abstract data of citation groups 

The `fetch_citationgroups` function will not vectorize the data into numpy arrays

data comes back as JSON

"""
#Copyright:
#License:

import json
import logging
import random
import sqlite3

import numpy as np
from pymongo import MongoClient

from .base import Bunch

VALIDATE_CITATION_GROUPS = set([
        "zero_citations",
        "one_to_five_citations",
        "six_to_ten_citations",
        "eleven_to_fifteen_citations",
        "sixteen_to_twenty_citations",
        "twenty_one_to_twenty_five_citations",
        "twenty_six_to_thirty_citations",
        "thirty_one_to_thirty_five_citations"
        "thirty_six_to_forty_citations",
        "forty_one_to_forty_five_citations",
        "forty_six_to_fifty_citaions",
        "fifty_one_to_fifty_five_citations",
        "fifty_six_to_sixty_citations",
        "sixty_one_to_sixty_five_citations",
        "sixty_six_to_seventy_citations",
        "seventy_one_to_seventy_six_citations",
        "seventy_six_to_eighty_citations",
        "eighty_one_to_eighty_five_citations",
        "eighty_six_to_ninety_citations",
])

#create MongoClient
try:

    client = MongoClient('localhost', 27017)

    db = client.pcite

    articles = db['articlemodels']


    conn = sqlite3.connect('data-articles.db')
    cursor = conn.cursor()

except Exception as e:
 	print(e)



def fetch_citationgroups(citation_groups=None):
	"""Load the citation group data and define data, target and 
	target_names attributes.

	Parameters
	----------

	citation_groups: None or collection of string or unicode
	    If None (default), load all the citation_groups.
	    If not None, list of citation_groups to load (other citation_groups
	    	ignore).


	"""

	
	data = Bunch()
	target = list()
	
	
	object_ids = list()
	
	if citation_groups is not None:
	
	#validate values of citation_groups before submitting to database
	    invalid_citation_group_name = {group for group in citation_groups if group not in VALIDATE_CITATION_GROUPS}

	    if len(invalid_citation_group_name) > 0:
	       return print("Invalid citation group name %s. Valid names are %s" 
	       	% (invalid_citation_group_name, VALIDATE_CITATION_GROUPS))

	    else:
	    	results = articles.find(
		    {"citation_group":
		    {'$in':citation_groups}},{"title":1, "abstract":1, "citation_group":1, "citation_count_at_two":1, "pmid":1})

	elif citation_groups is None: # get all groups

		results = articles.find({
			"citation_group": {"$exists": "true"}},
			{"title": 1, "abstract":1, "citation_group":1, "citation_count_at_two":1, "pmid":1})


	"""
	define data attributes 
	"""
	data.data = list(results) # chuck data into data attribute as a list. 
	#THEN SHUFFLE
	random.shuffle(data.data)
	"""target is the category label for each document. it's like an index and should
	be the same len as data.data attribute
	"""
	"""
	data.target should be indexable np.array e.g. np.array(target) of citation_groups for documents.
	e.g. data.target[0] should be citation_group label of data.data[0]
	BUT, I could spend too long figuring that out so I am using a list for now. 
	HOWEVER there is then no relationship between target and target_names that you get in sklearn.
	ALSO, will a list be a safe data type to use, as opposed to a tuple?
	"""
	data.target = [x.pop('citation_group') for x in data.data]
	data.object_ids = [x.pop('_id') for x in data.data]#removes ObjectIds from data
	data.citation_count = [x.pop('citation_count_at_two') for x in data.data]
	data.description = 'the citation_groups'
	data.target_names = results.distinct('citation_group') #using results cursor in event of citation_group=None
	data.pmid = [x.pop('pmid') for x in data.data]
	
	"""
	data.data should be an iterable which yields either str, unicode or file objects so...ugh...
	turn each dict object into a str object and later somehow remove {}
	"""
	data.data = [str(x) for x in data.data]
	
	
	 


	return data
