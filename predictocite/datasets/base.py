"""
Base IO code for citation_group datasets
heavily based on 
https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/base.py

"""


import numpy as np


class Bunch(dict):
	"""Container object for datasets: dictionary-like
	object that exposts its keys as attributes"""

	def __init__(self, **kwargs):
		dict.__init__(self, kwargs)
		self.__dict__ = self
		data = []
		target = []
		target_names = []
		object_ids = []
		description = ''
		citation_count = []
