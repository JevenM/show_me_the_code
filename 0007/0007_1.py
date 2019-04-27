# -*- coding: utf-8 -*-
import os

# 统计文件夹每个文件分别的注释、空行、代码行数

blank_lines = list()
annotation_lines = list()
code_lines = list()

def count_lines(filename):
    global blank_lines
    global code_lines
    global annotation_lines

    with open(filename, 'r', encoding='utf-8') as file:
        files = file.readlines()
        if files[-1][-1:] == '\n':
            print('???')
            blank_lines.append('\n')
        for line in files:
            _line = line.strip()
            if _line.startswith('#'):
                annotation_lines.append(_line)
            elif not _line:
                print('!!!')
                blank_lines.append(_line)
            else:
                code_lines.append(_line)


def show_result():
    global code_lines
    global annotation_lines
    global blank_lines

    print('-'*20)
    print('code: ', len(code_lines))

    for line in code_lines:
        print(line)

    print('-'*20)
    print('annotation: ', len(annotation_lines))
    for line in annotation_lines:
        print(line)

    print('-'*20)
    print('blank: ', len(blank_lines))
    for line in blank_lines:
        print(line)

    code_lines.clear()
    blank_lines.clear()
    annotation_lines.clear()


def process_files(filepath):
    files = os.listdir(filepath)
    for f in files:
        if f.endswith('.py'):
            filename = os.path.join(filepath, f)
            print('='*20)
            print('current file: ', filename)
            count_lines(filename)
            show_result()

if __name__ == '__main__':
    process_files('.')
