import hashlib
from collections import defaultdict
db={}
db = defaultdict(lambda: 'N/A')

def get_md5(password):
    a = hashlib.md5()
    a.update(password.encode('utf-8'))
    return (a.hexdigest())

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
    print(db[username])

def login(username, password):
    b = get_md5(password + username + 'the-Salt')
    print(b)
    if b == db[username]:
        return True
    else:
        return False

if __name__ == '__main__':
    a = input('注册输入用户名：')
    b = input('注册输入密码：')
    register(a, b)
    a = input('输入登录用户名：')
    b = input('输入登录密码：')
    print(login(a,b))

