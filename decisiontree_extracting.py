import numpy as np
from sklearn.tree import _tree

def tree_to_code(tree, feature_names, class_names):
	print 'Extracting the decision tree rules...'
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

if __name__ == '__main__':
	main()