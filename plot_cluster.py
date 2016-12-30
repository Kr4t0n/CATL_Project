import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
from sklearn.decomposition import IncrementalPCA
from scipy.cluster.hierarchy import dendrogram, linkage

def generating_KMeans_plot(n_clusters, X, y):
	print 'Generating KMeans plot...'
	colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
	labels = y.labels_
	cluster_centers = y.cluster_centers_
	
	''' Using PCA to transform the dataset X and cluster_centeres into two dimensional'''
	ipca = IncrementalPCA(n_components = 2, batch_size = 3)
	ipca.fit(X)
	X = ipca.transform(X)
	cluster_centers = ipca.transform(cluster_centers)
	
	''' Plot the result'''
	plt.close('all')
	plt.figure()
	plt.clf()
	for k, col in zip(range(n_clusters), colors):
		class_members = labels == k
		cluster_center = cluster_centers[k]
		plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
		plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor = col, markeredgecolor = 'k', markersize = 8)
		for x in X[class_members]:
			plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)
	plt.savefig('clustering_result/clustering-1.png', format = 'png')

def generating_Spectral_plot(n_clusters, X, y):
	print 'Generating Spectral plot...'
	colors = np.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
	colors = np.hstack([colors] * 20)
	labels = y.labels_
	
	''' Using PCA to transform the dataset X into two dimensional'''
	ipca = IncrementalPCA(n_components=2, batch_size=3)
	ipca.fit(X)
	X = ipca.transform(X)
	
	''' Plot the result'''
	plt.close('all')
	plt.figure()
	plt.clf()
	plt.scatter(X[:, 0], X[:, 1], color = colors[labels].tolist())
	plt.savefig('clustering_result/clustering-2.png', format = 'png')

def generating_Agglomerative_plot(n_clusters, X, y):
	print 'Generating Agglomerative plot...'
	
	# generate the linkage matrix
	Z = linkage(X, 'ward')
	
	''' Plot the result'''
	plt.close('all')
	plt.figure()
	plt.clf()
	dendrogram(Z, leaf_rotation = 90., leaf_font_size = 8.,)
	plt.savefig('clustering_result/clustering-3.png', format = 'png')
	
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