import re
import os

fpath = os.path.abspath('..')


def count_words(filepath, resultpath):
    fin = open(filepath, "r")
    fout = open(resultpath, "w+")
    str = fin.read()
    reObj = re.compile('\b?([a-zA-Z]+)\b?')
    words = reObj.findall(str)
    word_dict = {}
    lword=""
    uword=""
    for word in words:
        lword = word.lower()
        uword = word.upper()
        if word in word_dict:
            word_dict[lword] += 1
        else:
            word_dict[lword] = 1

    for (word, number) in word_dict.items():
        fout.write(word+":%d\n"%number)

if __name__ == '__main__':
    count_words(fpath + '/0004/text.txt', 'result.txt')

