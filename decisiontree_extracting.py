import numpy as np
from sklearn.tree import _tree
from db_operation import db_exec

index = 0
tree_index = 0
rule_index = 0

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
		global index
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
			index += 1
			fr.write(print_str)

	recurse(0, print_str)
	fr.close()

def tree_to_code_db(tree, feature_names, class_names, package_name):
	print 'Extracting the decision tree rules...'
	global rule_index
	global tree_index
	tree_index += 1
	tree_ = tree.tree_
	feature_name = [feature_names[i] if i != _tree.TREE_UNDEFINED else 'undefined!' for i in tree_.feature]
	rule_list = []
	database = 'catl'
	print 'Inserting the new result...'
	
	def recurse(node, database, package_name, rule_list):
		global rule_index
		if tree_.feature[node] != _tree.TREE_UNDEFINED:
			name = feature_name[node]
			threshold = tree_.threshold[node]
			condition_str = '{},<=,{}'.format(name, threshold)
			rule_list.append(condition_str.split(','))
			recurse(tree_.children_left[node], database, package_name, rule_list)
			condition_str = '{},>,{}'.format(name, threshold)
			rule_list.pop()
			rule_list.append(condition_str.split(','))
			recurse(tree_.children_right[node], database, package_name, rule_list)
		else:
			rule_index += 1
			result = class_names[np.argmax(tree_.value[node] / tree_.weighted_n_node_samples[node])]
			for i in range(len(rule_list)):
				sql = 'insert into dsresult values(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(package_name, tree_index, rule_index, rule_list[i][0], rule_list[i][1], rule_list[i][2], result)
				db_exec(database, sql)
	
	recurse(0, database, package_name, rule_list)
	rule_index = 0

if __name__ == '__main__':
	main()