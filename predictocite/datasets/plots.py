# -*- coding: utf-8 -*-
import pandas as pd

from ggplot import *
from pymongo import MongoClient



client = MongoClient('localhost', 27017)

db = client.pcite

articles = db['articlemodels']

results = articles.find({'citation_count_at_two':{'$exists':'true'}})
#count is 1644
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
gg + geom_histogram() + \
ggtitle("Figure 1: Histogram of number of citations at two years after publication") + \
labs("Number of citations", "Frequency")

# as fig one can't tell us much the data can can be limited
# to save on memory query the db again

results2 = articles.find({'citation_count_at_two':{'$exists':'true'},
	'citation_count_at_two':{'$lte':100}})

df2 = pd.DataFrame(list(results2))


gg2 = ggplot(aes(x='citation_count_at_two'), data=df)
gg2 + geom_histogram(binwidth=0.5) + \
scale_x_continuous(limits=[0,100], breaks=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) + \
ggtitle("Figure 2: Histogram of number of citations at two years after publication") + \
labs("Number of citations", "Frequency")