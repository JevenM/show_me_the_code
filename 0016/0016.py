import xlwt

with open('numbers.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    _numbers = eval(data)
    numbers = list()
    for i in range(3):
        numbers.extend(_numbers[i])

    row = len(numbers)//len(_numbers)

f = xlwt.Workbook()
table = f.add_sheet('numbers')
for i in range(len(numbers)):
	# 写入表格的时候的坐标
    table.write(i//row, i%row, numbers[i])

f.save('numbers.xls')


