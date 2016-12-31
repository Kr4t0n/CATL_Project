import pydot
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals.six import StringIO
from decisiontree_extracting import tree_to_code

def DSTree(X, y):
	print 'Generating Random Forest Classifier...'
	clf = RandomForestClassifier(n_estimators = 4)
	clf = clf.fit(X, y)
	
	print 'Different importances of each features: %s' % clf.feature_importances_
	
	print 'Generating Tree plot...'
	for i in xrange(len(clf.estimators_)):
		print 'Generating %d plot...' % i
		dot_data = StringIO()
		result_filename = 'classifying_result/classifying-{}.txt'.format(i)
		tree_to_code(clf.estimators_[i], feature_names = ['capacity', 'formation', 'imp', 'k', 'dcrfu25', 'dcr25', 'calendar60-30d', 'calendar60-60d', 'calendar60-120d', 'volume-80d', 'cycle45-300', 'cycle45-600', 'cycle45-900'], class_names = ['Good', 'Poor'], result_filename = result_filename)
		tree.export_graphviz(clf.estimators_[i], out_file = dot_data, feature_names = ['capacity', 'formation', 'imp', 'k', 'dcrfu25', 'dcr25', 'calendar60-30d', 'calendar60-60d', 'calendar60-120d', 'volume-80d', 'cycle45-300', 'cycle45-600', 'cycle45-900'], class_names = ['Good', 'Poor'], filled = True, rounded = True, special_characters = True, leaves_parallel = True)
		print 'Convering %d plot...' % i
		graph = pydot.graph_from_dot_data(dot_data.getvalue())
		graph[0].write_png('classifying_result/classifying-%d.png' % i)

if __name__ == '__main__':
	main()