import xlwt

with open('student.txt', 'r', encoding='GBK') as f:
	data = f.read()
	_student = eval(data)
	student = list()
	for i in range(1, 4):
		info = _student[str(i)]
		student.append(i)
		student.extend(info)
	print('len of _student: %d , len of student: %d' % (len(_student), len(student)))
	row = len(_student)/len(student)

def horz_left(x, y, data):
	alignt = xlwt.Alignment()
	alignt.horz = xlwt.Alignment.HORZ_LEFT
	style = xlwt.XFStyle()
	style.alignment = alignt
	tabl.write(x, y, data, style)

f = xlwt.Workbook()
tabl = f.add_sheet('student')
for i in range(len(student)):
	if not i % 5:
		horz_left(i//5, i%5, student[i])
	else:
		tabl.write(i//5, i%5, student[i])

f.save('student.xls')
