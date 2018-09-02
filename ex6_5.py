#!/usr/bin/env python3

import os
import json # NOQA


data = os.path.join(os.path.dirname(__file__), 'salt_contributors.json')


def your_function(datapath):
    '''Trả về list chứa các dictionary chứa data về các contributor bao gồm
    các key: login, html_url và contributions.
    Nếu html_url nào bị thiếu, tạo html_url mới bằng
    "https://github.com/" + login tương ứng.
    '''
    # Sửa function cho phù hợp, trả về kết quả yêu cầu.

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    with open(datapath, 'rt') as json_file:
        data_str = json_file.read()
        data = json.loads(data_str)
        list_user = []
        for dat in data:
            new_dict = {}
            new_dict['login'] = dat['login']
            if 'html_url' not in dat.keys() or dat['html_url'] == '':
                new_dict['html_url'] = "https://github.com/" + dat['login']
            else:
                new_dict['html_url'] = dat['html_url']
            new_dict['contributions'] = dat['contributions']
            list_user.append(new_dict)
    return list_user
    

def solve(input_data):
    result = your_function(input_data)

    return result


def main():
    '''Truy cập đường dẫn
    https://api.github.com/repos/saltstack/salt/contributors?page=3 Lưu lại
    thành file salt_contributors.json.
    Sử dụng JSON để chuyển dữ liệu thành dữ liệu trong Python.
    File đã được lưu sẵn trong thư mục này - link để đây để học viên biết
    dữ liệu lấy từ đâu.
    '''
    datafile = data

    for d in solve(datafile):
        print("User: {login} - URL {html_url} - {contributions}".format(**d))


if __name__ == "__main__":
    main()
