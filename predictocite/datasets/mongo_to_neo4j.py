from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.pcite

articles = db['articlemodels'] # a Collection

one_article = articles.find_one({'group':'base'}) #dict

references = one_article['references']#list

base_group = articles.find({'group':'base'})#cursor


for ref in one_article['references']:
	pmid = articles.find_one({'_id':ref})
	print(pmid['pmid'])# prints pmids of one_article's references



