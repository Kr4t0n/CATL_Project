import warnings
from decisiontree import DSTree
from db_operation import load_from_MySQL, write_to_MySQL
from file_operation import load_dataset
from standard import standard_dataset
from optparse import OptionParser

def parser_menu():
	''' Parser Process'''
	parser = OptionParser()
	parser.add_option('-t', '--table', dest = 'table_name', help = 'read data from db using table_name')
	parser.add_option('-f', '--file', dest = 'filename', help = 'read data from FILENAME')
	parser.add_option('-S', '--standard', action = 'store_true', dest = 'standard_verbose', default = False, help = 'standard the dataset')
	(options, args) = parser.parse_args()
	
	if options.table_name and options.filename:
		parser.error('Options -t and -f are mutually exclusive')
	elif options.table_name:
		barcode, X, y = load_from_MySQL(options.table_name)
		if options.standard_verbose:
			X = standard_dataset(X)
		DSTree(X, y)
	elif options.filename:
		X, y = load_dataset(options.filename)
		if options.standard_verbose:
			X = standard_dataset(X)
		DSTree(X, y)
	print 'Whole process successful!'

if __name__ == '__main__':
	# ignore the unnecessary warning
	warnings.filterwarnings('ignore')
	parser_menu()
