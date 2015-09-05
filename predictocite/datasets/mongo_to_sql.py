"""
Script for populating sqlite3 with simple article table
Data from MongoDB



"""

import sqlite3


from pymongo import MongoClient

#init sqlite connection and cursor
conn = sqlite3.connect('data-articles.db')
c = conn.cursor()

c.execute('''
	CREATE TABLE articles
	(id INTEGER PRIMARY KEY, title TEXT, abstract TEXT, citation_group VARCHAR, citation_count INTEGER, pmid INTEGER)
	''')

# init MongoDB client and db
client = MongoClient('localhost', 27017)

db = client.pcite

articles = db['articlemodels']
default = ''
id_value = 0

for doc in articles.find(
	{"citation_group": {"$exists":"true"}},
	{"title": 1, "abstract":1, "citation_group":1, 
	"citation_count_at_two":1, "pmid":1, "_id":0}):
    
    c.execute("INSERT INTO articles VALUES (?, ?, ?, ?, ?, ?)", 
    	(id_value, doc.get('title', default), doc.get('abstract', default), 
    		doc['citation_group'], doc['citation_count_at_two'],
    		doc['pmid'])
    	)
    id_value += 1
    

conn.commit()