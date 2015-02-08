#!/usr/bin/python
"""
populate_sentiments.py - renames files if they have matched sentiments.
Python 2.7.6
"""

import os

directory = (os.path.abspath(os.pardir) + "/raw_data/")
results_directory = os.path.abspath(os.pardir) + '/test_data/'
current_word = ""

with open(os.pardir+"/sentiments1.txt") as f:
	for line in f:
		line = line.strip()

		if line.isalpha() == True:
			current_word = line
		else:
			print("Current Word: {}").format(current_word)
			print("{} renamed to {}".format(''.join([directory, line, '_', '.txt']), "".join([results_directory, line, '_', current_word, '.txt'])))
			os.rename(''.join([directory, line, '_', '.txt']), "".join([results_directory, line, '_', current_word, '.txt']))