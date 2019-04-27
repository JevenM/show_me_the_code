import os
from hashlib import sha256
from hmac import HMAC

def encrypt_password(password, salt):
    if salt is None:
        salt = os.urandom(8)

    assert 8 == len(salt)

    if isinstance(password, str):
        password = password.encode('utf-8')
    if isinstance(salt, str):
    	salt = salt.encode('utf-8')

    result = password

    for i in range(10):
        result = HMAC(result, salt, sha256).digest()

    return salt + result

def validate_password(hashed, input_password):
    return hashed == encrypt_password(input_password, salt=hashed[:8])

if __name__ == '__main__':
    pwd = input('输入密码注册：')
    hashed = encrypt_password(pwd,'maogedmm')
    login_pwd = input('输入密码登录：')
    print(validate_password(hashed, login_pwd))

