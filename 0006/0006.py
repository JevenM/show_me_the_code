import os
import re
import glob
from collections import OrderedDict

def get_num(key_word, filename):
    fread = open(filename,'r', encoding='utf-8').read()
    re_zz = re.compile(r'[\s\,\;\.\n]{1}'+key_word+r'[\s\,\;\.\n]{1}')
    numbers = re_zz.findall(fread)
    return len(numbers)

def article_analysis(dirs):
    article = glob.glob(r'*.txt')
    dictdata = OrderedDict()
    for a in article:
        doc = open(a, 'r', encoding='utf-8').read()
        doc = re.findall(r'[\w\-\_\.\']+', doc)
        doc = list(map(lambda x: x.strip('.'), doc))

        for word in doc:
            dictdata[word] = get_num(word, a)

        d = OrderedDict(sorted(dictdata.items(), key=lambda x: x[1], reverse = True))
        print("在 %s 中出现次数最多的单词是：" % a)
        for c in d:
            print(c+' : %s 次' % d[c])
            break

        print('%s 次; %s 出现' % max(zip(d.values(), d.keys())))
    return 0

if __name__ == '__main__':
    file = '.'
    article_analysis(file)

