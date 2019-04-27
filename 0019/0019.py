import xlrd, codecs
from collections import OrderedDict
from lxml import etree


def read_xls(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    c = OrderedDict()
    for i in range(table.nrows):
        c[table.cell(i,0).value] = table.row_values(i)[1:]
    return c

def save_xml(data):
    output = codecs.open('numbers.xml', 'w', 'GBK')
    root = etree.Element('root')
    numbers_xml = etree.ElementTree(root)
    numbers = etree.SubElement(root, 'numbers')
    numbers.append(etree.Comment('数学'))
    numbers.text = str(data)
    output.write(etree.tounicode(numbers_xml.getroot()))
    output.close()

if __name__ == '__main__':
    f = 'numbers.xls'
    a = read_xls(f)
    save_xml(a)

