import copy
import numpy as np

def statistic_process(class_number, X, y, filename, barcode, feature_names):
	X_mean = []
	X_range = []
	
	class_member = y == class_number
	X_subset = X[class_member]
	barcode_subset = barcode[class_member]
	X_subsetmean = np.mean(X_subset, axis = 0)
	X_min = np.min(X_subset, axis = 0)
	X_max = np.max(X_subset, axis = 0)
	for idx in range(len(X_subsetmean)):
		X_mean.append(str(X_subsetmean[idx]))
	for idx in range(len(X_min)):
		range_string = '{}~{}'.format(X_min[idx], X_max[idx])
		X_range.append(range_string)
	
	# file writing process
	fr = open(filename, 'w')
	fr.write('Type,{}\n'.format(','.join(feature_names)))
	fr.write('Mean,{}\n'.format(','.join(X_mean)))
	fr.write('Range,{}\n'.format(','.join(X_range)))
	for idx in range(len(X_subset)):
		fr.write('{},{}\n'.format(barcode_subset[idx], ','.join(map(str, X_subset[idx]))))
	fr.close()

def statistic_KMeans(n_clusters, X, y, barcode, feature_names):
	print 'Generating KMeans statistic result...'
	
	X = np.array(X)
	barcode = np.array(barcode)
	for class_number in range(n_clusters):
		print 'Generating statistic result class {}...'.format(class_number)
		outfilename = 'clustering_result/clustering-1-{}.csv'.format(class_number)
		statistic_process(class_number, X, y.labels_, outfilename, barcode, feature_names)

def statistic_Spectral(n_clusters, X, y, barcode, feature_names):
	print 'Generating Spectral statistic result...'
	
	X = np.array(X)
	barcode = np.array(barcode)
	for class_number in range(n_clusters):
		print 'Generating statistic result class {}...'.format(class_number)
		outfilename = 'clustering_result/clustering-2-{}.csv'.format(class_number)
		statistic_process(class_number, X, y.labels_, outfilename, barcode, feature_names)

def statistic_Agglomerative(n_clusters, X, y, barcode, feature_names):
	print 'Generating Agglomerative statistic result...'
	
	X = np.array(X)
	barcode = np.array(barcode)
	for class_number in range(n_clusters):
		print 'Generating statistic result class {}...'.format(class_number)
		outfilename = 'clustering_result/clustering-3-{}.csv'.format(class_number)
		statistic_process(class_number, X, y.labels_, outfilename, barcode, feature_names)

def statistic_Ensemble(n_clusters, X, y, barcode, feature_names):
	print 'Generating Ensemble statistic result...'
	
	X = np.array(X)
	y = np.array(y)
	barcode = np.array(barcode)
	for class_number in range(n_clusters):
		print 'Generating statistic result class {}...'.format(class_number)
		outfilename = 'clustering_result/clustering-4-{}.csv'.format(class_number)
		statistic_process(class_number, X, y, outfilename, barcode, feature_names)

if __name__ == '__main__':
	main()