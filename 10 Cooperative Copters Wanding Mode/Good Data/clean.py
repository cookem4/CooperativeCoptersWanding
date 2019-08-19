import sys

if __name__ == "__main__":
	with open(sys.argv[1], 'r') as f:
		line = f.readline()

		line = f.readline().split('\t')
		while len(line) > 1:
			test = line[:-1]
			print(','.join(test))
			line = f.readline().split('\t')