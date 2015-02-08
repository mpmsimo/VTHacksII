#!/usr/bin/python
"""
format_chat_log.py - Companion script for format_xchat_log.sh.
msimo - 2/6/15 - VTHacksII
Python 2.7.6
"""

import sys, os

directory = (os.path.abspath(os.pardir))
dir2 = directory + "/raw_data"
print directory, dir2
dir3 = directory + "/chat_transcript/"

def write_files(filename):
	counter = len(os.listdir(dir2)) + 1
	print("write_files >> Count: {}".format(counter))
	with open(filename) as f:
		print("Opened file: {}".format(filename))
		for line in f:
			new_file = ("{}_.txt").format(counter)
			f2 = open(new_file, 'w+')
			f2.write(line)
			f2.close()
			print("Created file: {}".format(new_file))
			counter += 1

def main():
	print("Dir1: {}\nDir2: {}\nDir3: {}".format(directory, dir2, dir3)) 
	filename = sys.argv[1]
	write_files(os.path.join(dir3, filename))
"""
	for filename in os.listdir(dir3):
		print("main >> Opened file: {}".format(filename))
		if filename.endswith(".txt"):
			write_files(os.path.join(dir3, filename))
"""

if __name__ == "__main__":
	main()