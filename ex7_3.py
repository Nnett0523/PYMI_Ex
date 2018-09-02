#!/usr/bin/env python3


__doc__ = '''
Yêu cầu:
- Lưu file ``https://raw.githubusercontent.com/hvnsweeting/states/master/salt/event/init.sls`` về máy với tên event.yaml

- Dùng pip cài thư viện PyYAML, import yaml và dùng `yaml.load` để biến nội
dung trong file thành kiểu dữ liệu trên Python.

- In ra số phần tử của kiểu dữ liệu vừa tạo. Dùng thư viện json để
 `json.dump` nội dung, ghi ra một file tên là event.json trong thư mục hiện tại.

- Dùng thư viện pickle để pickle.dump nội dung trên ra file event.pkl trong
  thư mục hiện tại. Chú ý khi mở file, phải mở ở chế độ ghi ở dạng binary. Đọc
  thêm tại đây:
  https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files`

- In ra kích thước của mỗi file đã tạo.

Gợi ý: sử dụng os.stat(filename).st_size
'''  # NOQA


import json  # NOQA
import os  # NOQA
import pickle  # NOQA
import yaml  # NOQA


def your_function():
    '''Trả về số phần tử của kiểu dữ liệu sau khi dùng module `yaml` để load

    Thực hiện các yêu cầu tại ``__doc__``

    :rtype int:
    '''
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    yaml_filename = '../exercises/event.yaml'
    json_filename = '../exercises/event.json'
    pickle_filename = '../exercises/event.pkl'

    with open(yaml_filename, 'rt') as f:
        yaml_data = yaml.safe_load(f.read())
    print(len(yaml_data.keys()))
    with open(json_filename, 'w') as f:
        f.write(json.dumps(yaml_data))
    with open(pickle_filename, 'wb') as f:
        pickle.dump(yaml_data, f)

    print('The size of {} is {}'.format(yaml_filename, \
                                    os.stat(yaml_filename).st_size))
    print('The size of {} is {}'.format(json_filename, \
                                    os.stat(json_filename).st_size))
    print('The size of {} is {}'.format(pickle_filename, \
                                os.stat(pickle_filename).st_size))

    result = yaml_data

    return result


def solve():
    '''Học viên không cần viết code trong hàm `solve`, chỉ thực hiện
    đổi tên lại function của mình cho phù hợp

    :rtype int:
    '''
    result = your_function()

    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
