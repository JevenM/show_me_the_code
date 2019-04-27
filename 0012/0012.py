import os
import re

# 敏感词汇替换成**，写死了，无论几个字符

def filter_word(w):
    sensitive = False
    strs = '**'
    f = open('filtered_words.txt', 'r', encoding='utf-8').readlines()
    for i in f:
        i = i.strip()
        b = re.split(r'%s' % (i), w)
        if len(b) > 1:
            c = i
            sensitive = True
        else:
            pass

    if sensitive == True:
        b = re.split(r'%s' % (c.strip()), w)
        print(strs.join(b))
    else:
        print(w)
    return 0

if __name__ == '__main__':
    word = input('请输入：')
    filter_word(word)
