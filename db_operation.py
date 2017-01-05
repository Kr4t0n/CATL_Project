import MySQLdb

def load_from_MySQL(table_name):
	""" load dataset from database using serial number"""
	print 'Loading the dataset from db...'
	conn = MySQLdb.connect(user = 'root', passwd = 'password', host = '127.0.0.1')
	conn.select_db('catl')
	curr = conn.cursor()
	sql = 'select * from ' + str(table_name)
	try:
		curr.execute(sql)
		result = curr.fetchall()
	except:
		print 'Error: unable to fetch battery data'
	curr.close()
	conn.close()
	
	''' turn type(result) = tuple into type(result) = list'''
	result = list(result)
	for idx in range(len(result)):
		result[idx] = list(result[idx])
	
	''' split result into X and y'''
	barcode = []
	X = []
	y = []
	for idx in range(len(result)):
		barcode.append(result[idx][0])
		X.append(result[idx][1:-2])
		y.append(result[idx][-2])
	
	''' change the type of X and y'''
	X = map(lambda t: map(float, t), X)
	return barcode, X, y

def write_to_MySQL(table_name, barcode, final_clusters):
	''' write the dataset result into database using serial number'''
	print 'Writing the result into db...'
	conn = MySQLdb.connect(user = 'root', passwd = 'password', host = '127.0.0.1')
	conn.select_db('catl')
	for idx in range(len(barcode)):
		curr = conn.cursor()
		sql = 'update ' + str(table_name) + ' set result=\'' + str(final_clusters[idx]) + '\' where barcode=\'' + str(barcode[idx]) + '\''
		try:
			curr.execute(sql)
		except:
			print 'Error: unable to update the result'
		conn.commit()
		curr.close()
	conn.close()

def load_property_from_MySQL(table_name):
	# load the featrure_names and class_names from MySQL using table_name
	print 'Loading feature_names and class_names...'
	feature_names = []
	class_names = []
	conn = MySQLdb.connect(user = 'root', passwd = 'password', host = '127.0.0.1')
	conn.select_db('catl')
	curr = conn.cursor()
	sql = 'select column_name from information_schema.COLUMNS where table_name=\'{}\''.format(table_name)
	try:
		curr.execute(sql)
		result = curr.fetchall()
	except:
		print 'Error: unable to fetch feature_names and class_names'
	# Eliminate the barcode, result and class and turn into list
	feature_names_temp = map(list, result)[1:-2]
	for idx in range(len(feature_names_temp)):
		feature_names.append(feature_names_temp[idx][0])
	
	# Get the class_names in order
	sql = 'select result from {}'.format(table_name)
	try:
		curr.execute(sql)
		result = curr.fetchall()
	except:
		print 'Error: unable to fetch the result data'
	result_set = set(result)
	for idx in range(len(result_set)):
		sql = 'select class from {} where result={}'.format(table_name, idx)
		try:
			curr.execute(sql)
			result = curr.fetchone()
		except:
			print 'Error: unable to fetch the class'
		class_names.append(*result)
	curr.close()
	conn.close()
	return feature_names, class_names

if __name__ == '__main__':
	load_property_from_MySQL(table_name = 'battery1')