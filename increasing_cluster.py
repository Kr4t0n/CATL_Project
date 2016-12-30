import copy

def tran_increase(array1):
	replaced = copy.deepcopy(array1)
	set1 = set(array1)
	u1 = list(set1)
	
	criteria_list = range(len(u1))
	tran_dict = {}
	
	for idx in range(len(array1)):
		if array1[idx] in u1:
			tran_dict[array1[idx]] = criteria_list[0]
			u1.pop(u1.index(array1[idx]))
			criteria_list.pop(0)
	
	for idx in range(len(replaced)):
		replaced[idx] = tran_dict[replaced[idx]]
	return replaced

if __name__ == '__main__':
	array1 = [3, 4, 4, 2, 0]
	print tran_increase(array1)