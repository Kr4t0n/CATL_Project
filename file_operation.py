def load_dataset(fileName):
	""" load the dataset from csv file """
	fr = open(fileName)
	# X is attribute
	# y is target
	X = []
	y = []
	i = 0
	for line in fr.readlines():
		curLine = line.strip().replace(' ','').split(',')
		if i == 0:
			# the first line is the features_name
			i = 1
			features_name = curLine[1:-1]
		else:
			xtemp = curLine[1:-1]
			X.append(xtemp)
			y.append(curLine[-1])
	return X, y