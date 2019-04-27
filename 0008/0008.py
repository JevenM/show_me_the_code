# -*- coding: utf-8 -*-
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    body = False
    newLine = False

    def handle_starttag(self, tag, attrs):
        if ('class', 'zh-summary summary clearfix') in attrs and tag == 'div':
            self.body = True
        elif ('class', 'zm-editable-content clearfix') in attrs and tag == 'div':
            self.body = True
        elif tag == 'br':
            print('\n')
        else:
            self.body = False

    def handle_data(self, data):
        if self.body:
            print(data.strip())
        else:
            pass


if __name__ == '__main__':
    parser = MyHTMLParser()
    f = open('test.html', 'r', encoding='gbk').read()
    parser.feed(f)


