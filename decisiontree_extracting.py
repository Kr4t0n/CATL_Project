import numpy as np
from sklearn.tree import _tree

def tree_to_code_depth(tree, feature_names, class_names, result_filename):
	print 'Extracting the decision tree rules...'
	fr = open(result_filename, 'w')
	tree_ = tree.tree_
	feature_name = [feature_names[i] if i != _tree.TREE_UNDEFINED else 'undefined!' for i in tree_.feature]

	def recurse(node, depth):
		indent = '    ' * depth
		if tree_.feature[node] != _tree.TREE_UNDEFINED:
			name = feature_name[node]
			threshold = tree_.threshold[node]
			fr.write('{}if {} <= {}:\n'.format(indent, name, threshold))
			recurse(tree_.children_left[node], depth + 1)
			fr.write('{}else:  # if {} > {}\n'.format(indent, name, threshold))
			recurse(tree_.children_right[node], depth + 1)
		else:
			fr.write('{}return {} \n'.format(indent, class_names[np.argmax(tree_.value[node] / tree_.weighted_n_node_samples[node])]))

	recurse(0, 0)
	fr.close()

def tree_to_code(tree, feature_names, class_names, result_filename):
	print 'Extracting the decision tree rules...'
	fr = open(result_filename, 'w')
	tree_ = tree.tree_
	feature_name = [feature_names[i] if i != _tree.TREE_UNDEFINED else 'undefined!' for i in tree_.feature]
	print_str = 'if '
	
	def recurse(node, print_str):
		if tree_.feature[node] != _tree.TREE_UNDEFINED:
			name = feature_name[node]
			threshold = tree_.threshold[node]
			condition_str = '{} <= {}, '.format(name, threshold)
			recurse(tree_.children_left[node], print_str + condition_str)
			condition_str = '{} > {}, '.format(name, threshold)
			recurse(tree_.children_right[node], print_str + condition_str)
		else:
			return_str = ' return {}\n'.format(class_names[np.argmax(tree_.value[node] / tree_.weighted_n_node_samples[node])])
			print_str = print_str[:-2] + return_str
			fr.write(print_str)
	
	recurse(0, print_str)
	fr.close()

if __name__ == '__main__':
	main()