# -*- coding: utf-8 -*-
import pandas as pd

from ggplot import *
from pymongo import MongoClient



client = MongoClient('localhost', 27017)

db = client.pcite

articles = db['articlemodels']

results = articles.find({'citation_count_at_two':{'$exists':'true'}})

# results needs to be a list so it can be passed to a dataframe. data argument can't be an iterator

df = pd.DataFrame(list(results))

# remove some columns that aren't needed
dropped_columns = ['link', 'sub_group', 'references', 
				'volume', 'spage', 'journal', 
				'pmcid', 'is_ref_of', '_id', 
				'__v', 'free_access', 'license', 'group']

df.drop(dropped_columns, axis=1, inplace=True)
#figure_1.png
gg = ggplot(aes(x='citation_count_at_two'), data=df)
gg + geom_histogram() + ggtitle("Histogram of number of citations at two years after publication") 
	+ labs("Number of citations", "Frequency")