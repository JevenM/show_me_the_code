import xlwt


with open('city.txt', 'r', encoding='GBK') as f:
    data = f.read()
    _city = eval(data)
    city = list()
    for i in range(1, 4):
        info = _city[str(i)]
        city.append(i)
        city.append(info)
    row = len(city)//len(_city)


def horz_left(x, y, data):
    alignt = xlwt.Alignment()
    alignt.horz = xlwt.Alignment.HORZ_LEFT
    style = xlwt.XFStyle()
    style.alignment = alignt
    table.write(x, y, data, style)

f = xlwt.Workbook()
table = f.add_sheet('city')
for i in range(len(city)):
    if not i % row:
        horz_left(i//row, i%row, city[i])
    else:
        table.write(i//row, i%row, city[i])

f.save('city.xls')
