input1 = input{'Apakah kamu belajar? (ya/tidak)')
input2 = input('Apakah kamu deadliner? (ya/tidak)")

if input1.lower() == 'ya':
	belajar = True
else:
	belajar = False
	
if input2.lower() == 'ya':
	deadliner = True
else:
	deadliner = False

if belajar = True:
	if deadliner == False:
		tubes_selesai = True
	else:
		tubes_selesai = False
else:
	tubes_selesai = false
	
if tubes_selesai:
	print('Hore tubes kamu selesai! :D')
elif tubes_selesai == talse:
	print('Yah tubesnya gak selesai :(')