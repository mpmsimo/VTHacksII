#!/usr/bin/python
"""
format_bash_log.py - Companion script for format_xchat_log.sh.
msimo - 2/6/15 - VTHacksII
Python 2.7.6
"""

import sys, os
filename = sys.argv[1]
#directory = "../raw_data/"
directory = os.path.abspath(os.pardir+"/raw_data/")

def write_files():
	count = len(os.walk(directory).next()[2]) + 1
	print("Count: {}".format(count))
	with open(filename) as f:
		print("Opened file: {}".format(filename))
		for line in f:
			new_file = ("{}_.txt").format(count)
			f2 = open(new_file, 'w+')
			f2.write(line)
			print("Created file: {}".format(new_file))
			count = count + 1

def main():
	#count2 = len(os.walk(directory).next()[2])
	#print("Directory: {}\nCount: {}".format(directory, count2))
	write_files()

if __name__ == "__main__":
	main()