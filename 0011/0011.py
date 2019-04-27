import os
import re

def filter_word(w):
    f = open('filtered_words.txt', encoding='utf-8').read()
    if w == '':
        print('Human Rights!')
    elif len(re.findall(r'%s' % (w), f)) == 0:
        print('Human Rights!')
    else:
        print('Freedom!')

if __name__ == '__main__':
    word = input('请输入词语：')
    filter_word(word)
