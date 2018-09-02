#!/usr/bin/env python3

import random  # NOQA
import string  # NOQA


def make_a_pwd(length=16):
    '''Tạo một mật khẩu ngẫu nhiên (random password),
    mật khẩu này bắt buộc phải chứa ít nhất 1 chữ thường,
    1 chữ hoa, 1 số, 1 ký tự punctuation (string.punctuation).
    '''
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    pwd = ''
    pwd += random.choice(string.ascii_lowercase)
    pwd += random.choice(string.ascii_uppercase)
    pwd += random.choice(string.digits)
    pwd += random.choice(string.punctuation)

    _others = string.ascii_letters + \
                string.digits + \
                string.punctuation
    
    for i in range(length-4):
        pwd += random.choice(_others)

    return pwd

def generate_and_append(length, passwords=[]):
    '''
    Sinh password ngẫu nhiên và append vào list passwords.
    Nếu không có list nào được gọi với function, trả về list chứa một
    password vừa tạo ra.
    Sửa argument tùy ý.
    '''
    password = make_a_pwd(length)
    if not passwords:
        return [password]
    else:
        passwords.append(password)
        return passwords

def solve(input_data):
    result = make_a_pwd(input_data)
    return result


def main():
    '''
    Sinh ra 10 password và viết code đảm bảo chúng đều khác nhau.
    '''
    passwords8 = generate_and_append(8)
    passwords10 = generate_and_append(10)
    passwords12 = generate_and_append(12)

    passwords12 = generate_and_append(12, passwords12)

    assert len(passwords8) == 1, passwords8
    assert len(passwords10) == 1, passwords10
    assert len(passwords12) == 2, passwords12

    for ps in passwords8, passwords10, passwords12:
        for p in ps:
            plen = len(p)
            print('Mậu khẩu tự tạo {0} ký tự của bạn là {1}'.format(plen, p))


if __name__ == "__main__":
    main()
