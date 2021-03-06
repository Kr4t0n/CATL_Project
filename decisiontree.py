import pydot
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals.six import StringIO
from db_operation import db_exec
from decisiontree_extracting import tree_to_code, tree_to_code_db

def DSTree(X, y, feature_names, class_names):
	# Undefined input variable
	package_name = 'EPP-14-225'
	
	print 'Generating Random Forest Classifier...'
	clf = RandomForestClassifier(n_estimators = 4)
	clf = clf.fit(X, y)
	
	# print 'Different importances of each features: %s' % clf.feature_importances_
	print 'Removing the old package result...'
	sql = 'delete from dsresult where package=\'{}\''.format(package_name)
	db_exec('catl', sql)
	print 'Generating Tree plot...'
	for i in xrange(len(clf.estimators_)):
		dot_data = StringIO()
		# result_filename = 'classifying_result/classifying-{}.txt'.format(i)
		# tree_to_code(clf.estimators_[i], feature_names = feature_names, class_names = class_names, result_filename = result_filename)
		tree_to_code_db(clf.estimators_[i], feature_names = feature_names, class_names = class_names, package_name = package_name)
		print 'Generating %d plot...' % i
		tree.export_graphviz(clf.estimators_[i], out_file = dot_data, feature_names = feature_names, class_names = class_names, filled = True, rounded = True, special_characters = True, leaves_parallel = True)
		print 'Convering %d plot...' % i
		graph = pydot.graph_from_dot_data(dot_data.getvalue())
		graph[0].write_png('classifying_result/classifying-%d.png' % i)

if __name__ == '__main__':
	main()