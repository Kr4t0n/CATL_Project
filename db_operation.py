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
		X.append(result[idx][1:-1])
		y.append(result[idx][-1])
	
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

if __name__ == '__main__':
	main()