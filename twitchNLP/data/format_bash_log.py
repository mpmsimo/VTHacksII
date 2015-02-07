filename = 'twitch_test2.log'
directory = "1618"
def write_files():
	count = 1
	with open(filename) as f:
		print("Opened file: {}".format(filename))
		for line in f:
			new_file = ("./lines/1618/{}_.txt").format(count)
			f2 = open(new_file, 'w+')
			f2.write(line)
			print("Created file: {}".format(new_file))
			count = count +1

def main():
	write_files()

if __name__ == "__main__":
	main()