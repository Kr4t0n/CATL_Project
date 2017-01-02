import numpy as np

def statistic_process(class_number, X, y, filename):
	X_mean = []
	X_range = []
	
	class_member = y == class_number
	X_subset = X[class_member]
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
	fr.write('Mean:\t{}\n'.format(str(X_mean)))
	fr.write('Range:\t{}\n'.format(str(X_range)))
	

def statistic_KMeans(n_clusters, X, y):
	print 'Generating KMeans statistic result...'
	
	X = np.array(X)
	for class_number in range(n_clusters):
		print 'Generating statistic result class {}...'.format(class_number)
		outfilename = 'clustering_result/clustering-1-{}.txt'.format(class_number)
		statistic_process(class_number, X, y.labels_, outfilename)

def statistic_Spectral(n_clusters, X, y):
	print 'Generating Spectral statistic result...'
	
	X = np.array(X)
	for class_number in range(n_clusters):
		print 'Generating statistic result class {}...'.format(class_number)
		outfilename = 'clustering_result/clustering-2-{}.txt'.format(class_number)
		statistic_process(class_number, X, y.labels_, outfilename)

def statistic_Agglomerative(n_clusters, X, y):
	print 'Generating Agglomerative statistic result...'
	
	X = np.array(X)
	for class_number in range(n_clusters):
		print 'Generating statistic result class {}...'.format(class_number)
		outfilename = 'clustering_result/clustering-3-{}.txt'.format(class_number)
		statistic_process(class_number, X, y.labels_, outfilename)

def statistic_Ensemble(n_clusters, X, y):
	print 'Generating Ensemble statistic result...'
	
	X = np.array(X)
	y = np.array(y)
	for class_number in range(n_clusters):
		print 'Generating statistic result class {}...'.format(class_number)
		outfilename = 'clustering_result/clustering-4-{}.txt'.format(class_number)
		statistic_process(class_number, X, y, outfilename)

def generating_Ensemble_plot(n_clusters, X, y):
	print 'Generating Ensemble plot...'
	colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
	labels = np.array(y)
	
	''' Using PCA to transform the dataset X and cluster_centeres into two dimensional'''
	ipca = IncrementalPCA(n_components = 2, batch_size = 3)
	ipca.fit(X)
	X = ipca.transform(X)
	
	''' Plot the result'''
	plt.close('all')
	plt.figure()
	plt.clf()
	for k, col in zip(range(n_clusters), colors):
		markersize = 14 - 4 * k 
		class_members = labels == k
		plt.plot(X[class_members, 0], X[class_members, 1], 'o', markerfacecolor = col, markeredgecolor = 'k', markersize = markersize)
	plt.savefig('clustering_result/clustering-4.png', format = 'png')

if __name__ == '__main__':
	main()