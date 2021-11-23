def find_accuracy(y_predict, y_test):
	clut = {}
	for i,y in enumerate(y_test):
		if y not in clut:
			temp = {}
			temp[y_predict[i]] = 1
			clut[y] = temp
		else:
			temp = clut[y]
			if y_predict[i] not in temp:
				temp[y_predict[i]] = 1
				clut[y] = temp
			else:
				temp[y_predict[i]] = temp[y_predict[i]] + 1
				clut[y] = temp
	count_true_predict = 0
	for key in clut:
		cluster = clut[key]
		dominan_label = 0
		for key_2 in cluster:
			if dominan_label < cluster[key_2]:
				dominan_label = cluster[key_2]
		count_true_predict += dominan_label
	return(count_true_predict / len(y_test))