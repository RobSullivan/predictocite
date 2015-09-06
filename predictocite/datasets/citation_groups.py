"""Loader for the citation groups from sqlite3

modelled on https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/twenty_newsgroups.py#L151

sqlite3 code from https://docs.python.org/3.4/library/sqlite3.html

This dataset loader will retrieve title, abstract, citation_group and pmid data of articles 

The `fetch_citationgroups` function will not vectorize the data into numpy arrays as it does in scikit-learn

"""
#Copyright:
#License:

import json
import logging
import random
import sqlite3


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

#create database connection
try:

    
    conn = sqlite3.connect('data\data-articles.db')
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
	
	
	
	
	if citation_groups is not None:
	
	#validate values of citation_groups before submitting to database
	    invalid_citation_group_name = {group for group in citation_groups if group not in VALIDATE_CITATION_GROUPS}

	    if len(invalid_citation_group_name) > 0:
	       return print("Invalid citation group name %s. Valid names are %s" 
	       	% (invalid_citation_group_name, VALIDATE_CITATION_GROUPS))

	    else:
	    	#not ideal because uses placeholder instead of param substitution http://stackoverflow.com/questions/283645/python-list-in-sql-query-as-parameter
	    	placeholder = '?'
	    	placeholders = ', '.join(placeholder for i in citation_groups)
	    	query = 'SELECT title, abstract, citation_group, pmid FROM articles WHERE citation_group in (%s)' % placeholders
	    	results_sql = cursor.execute(query, citation_groups)

	
	elif citation_groups is None: # get all groups

		results_sql = cursor.execute('SELECT title, abstract, citation_group, pmid FROM articles') 

	
	data.data = []
	data.target = []
	data.target_names = VALIDATE_CITATION_GROUPS
	data.pmid = []

	for title, abstract, citation_group, pmid in results_sql:
		data.data.append(title + ' ' + abstract)
		data.target.append(citation_group)
		data.pmid.append(pmid)


	return data
