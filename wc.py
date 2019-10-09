def linecount(filename):
	count = 0
	for line in open(filename):
		count += 1
	return count

if __name__ == '__main__':
	print(linecount('wc.py'))
else:
	print('__name__ = '+__name__)

def test():
	print('xx = '+str(linecount('wc.py')))