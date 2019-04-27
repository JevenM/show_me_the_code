import os
import re
import xlrd

def jishu(file):
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]
    re_timesec = re.compile(r'([\d]+)秒')
    re_timesec = re.compile(r'([\d]+)分')
    row_nums = table.nrows
    numbers = 0
    for i in range(0, row_nums):
        a = re_timesec.findall(table.cell(i,3).value)
        if len(a) == 0:
            pass
        else:
            numbers += int(a[0])
        if len(b) == 0:
            pass
        else:
            numbers += int(b[0])*60

    print('您本月通话时长总时：%s 分 %s 秒' % (numbers//60, numbers%60))

file = '语音通信.xls'
jishu(file)

