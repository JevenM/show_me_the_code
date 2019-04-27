﻿import os
import re

# 统计一个文件夹所有的代码、空行、注释

def count_num(filepath, filename):
    rownum = [0, 0, 0]
    path = os.path.join(filepath, filename)
    flines = open(path, 'r', encoding='utf-8').readlines()

    for i in flines:
        if re.match(r'^#', i) == None: #获得注释行数
            pass
        else:
            rownum[1] += 1

    if flines[-1][-1:] == '\n': #最后一行为空行
        rownum[2] = flines.count('\n') + 1 #获得空行行数
        rownum[0] = len(flines) + 1 - rownum[2] - rownum[1] # 代码行数
    else:
        rownum[2] = flines.count('\n')
        rownum[0] = len(flines) - rownum[2] - rownum[1]
    return rownum

def file_analysis(filepath, extension):
    pyfiles = [x for x in os.listdir(filepath) if os.path.splitext(x)[1] == extension] #扩展名为.py的文件列表
    print(pyfiles)
    the_num = [0, 0, 0]
    for i in pyfiles:
        num = count_num(filepath, i)
        the_num[0] += num[0]
        the_num[1] += num[1]
        the_num[2] += num[2]

    print('''统计目录中：
    代码有 %s 行
    注释有 %s 行
    空行有 %s 行
    ''' % (the_num[0], the_num[1], the_num[2]))

if __name__ == '__main__':
    file = '.'
    ext = '.py'
    file_analysis(file, ext)
