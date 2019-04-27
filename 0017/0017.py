import xlrd, codecs
from lxml import etree
from collections import OrderedDict

def read_xls(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    c = OrderedDict()
    for i in range(table.nrows):
        c[table.cell(i,0).value] = table.row_values(i)[1:]
    print(c)
    return c

def save_xml(data):
    output = codecs.open('student.xml', 'w', 'GBK')
    root = etree.Element('root')
    student_xml = etree.ElementTree(root)
    student = etree.SubElement(root, 'students')
    student.append(etree.Comment('学生信息表\n\"id\" : [名字, 数学, 语文, 英语]'))
    student.text = str(data)
    output.write(etree.tounicode(student_xml.getroot()))
    output.close()

if __name__ == '__main__':
    f = 'student.xls'
    a = read_xls(f)
    save_xml(a)


