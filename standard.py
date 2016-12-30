import numpy as np
from sklearn import preprocessing

def standard_dataset(X):
	print 'Preprocessing the dataset...'
	X_scaled = preprocessing.scale(X)
	
	return X_scaled

if __name__ == '__main__':
	main()