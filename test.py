a = [1,2,3]
	
for i in range(len(a)):
	a[i] += 3
	
for numb in a:
	print(numb)
	
print(a is list)
print(1 is int)
print(isinstance(a, list))