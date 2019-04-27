# -*- coding: utf-8 -*-
import mysql.connector


def store_data(filepath):
    conn = mysql.connector.connect(user='root', password='1234', database='showCode')
    cursor = conn.cursor()
    
    cursor.execute('show tables in showCode;')
    tables = cursor.fetchall()
    findtables = False
    for table in tables:
        if 'code' in table:
            findtables = True
    if not findtables:
        cursor.execute('''
            create table code(
                id int not null auto_increment,
                code varchar(10) not null,
                primary key(id)
            );
        ''')

    f = open(filepath, 'rb')
    for line in f.readlines():
        code = line.strip()
        cursor.execute('insert into showCode.code (code) values(%s);', [code])
    
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    store_data('../0001/generateCode.txt')
    
