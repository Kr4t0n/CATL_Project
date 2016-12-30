import pydot
import numpy as np
from sklearn import tree
from sklearn.tree import _tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals.six import StringIO

def tree_to_code(tree, feature_names, class_names):
	tree_ = tree.tree_
	feature_name = [feature_names[i] if i != _tree.TREE_UNDEFINED else 'undefined!' for i in tree_.feature]
	print 'def tree({}):'.format(','.join(feature_names))
	
	def recurse(node, depth):
		indent = ' ' * depth
		if tree_.feature[node] != _tree.TREE_UNDEFINED:
			name = feature_name[node]
			threshold = tree_.threshold[node]
			print "{}if {} <= {}:".format(indent, name, threshold)
			recurse(tree_.children_left[node], depth + 1)
			print "{}else:  # if {} > {}".format(indent, name, threshold)
			recurse(tree_.children_right[node], depth + 1)
		else:
			print "{}return {}".format(indent, class_names[np.argmax(tree_.value[node] / tree_.weighted_n_node_samples[node])])
	
	recurse(0, 1)

def DSTree(X, y):
	print 'Generating Random Forest Classifier...'
	clf = RandomForestClassifier(n_estimators = 4)
	clf = clf.fit(X, y)
	# dot_data = StringIO()
	
	print 'Different importances of each features: %s' % clf.feature_importances_
	
	print 'Generating Tree plot...'
	for i in xrange(len(clf.estimators_)):
		print 'Generating %d plot...' % i
		dot_data = StringIO()
		tree_to_code(clf.estimators_[i], feature_names = ['capacity', 'formation', 'imp', 'k', 'dcrfu25', 'dcr25', 'calendar60-30d', 'calendar60-60d', 'calendar60-120d', 'volume-80d', 'cycle45-300', 'cycle45-600', 'cycle45-900'], class_names = ['Good', 'Poor'])
		tree.export_graphviz(clf.estimators_[i], out_file = dot_data, feature_names = ['capacity', 'formation', 'imp', 'k', 'dcrfu25', 'dcr25', 'calendar60-30d', 'calendar60-60d', 'calendar60-120d', 'volume-80d', 'cycle45-300', 'cycle45-600', 'cycle45-900'], class_names = ['Good', 'Poor'], filled = True, rounded = True, special_characters = True, leaves_parallel = True)
		print 'Convering %d plot...' % i
		graph = pydot.graph_from_dot_data(dot_data.getvalue())
		graph[0].write_png('classifying_result/classifying-%d.png' % i)

if __name__ == '__main__':
	main()