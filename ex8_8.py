#!/usr/bin/env python3

__doc__ = '''
Viết script get_version nhận vào ngày ở format <month>/<day>/<year>.
VD: 03/28/16 làm parameter và in ra một version được tính theo quy luật sau:
- Version ở dạng format: <MAJOR>.<MINOR>.<PATCH>, vd: "6.9.2"
- Cách đánh version này gọi là semver http://semver.org/
- Từ ngày 09 tháng 02 năm 2016, phiên bản bắt đầu là "1.0.0"
- Mỗi 28 ngày, MAJOR lại tăng thêm 1, MINOR và PATCH set về 0
- Mỗi 7 ngày, MINOR tăng thêm 1 và PATCH sẽ set về 0
- Cứ mỗi ngày, PATCH lại tăng thêm 1.

In ra phiên bản tương ứng.

Gợi ý: học viên sử dụng `sys.argv` hoặc module `argparse`
'''

import log
import sys
from datetime import datetime
from datetime import timedelta
logger = log.get_logger(__name__)


def your_function(input_data):  # gia su nhan vao: "02/03/16", "09/06/16"
    '''Trả về tên phiên bản như yêu cầu tại ``__doc__``

    :param input_data: ngày format ở dạng <month>/<day>/<year>,
                       ví dụ: "02/03/16"
    :rtype str:
    '''
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    result = None

    begin_day = '02/09/16'  # => version: 1.0.0
    begin_day = datetime.strptime(begin_day, '%m/%d/%y')
    # tim day co version 0.0.0
    delta_time = timedelta(28)
    zero_version_day = begin_day - delta_time  # => version: 0.0.0

    # convert the input_data to format
    current_version_day = datetime.strptime(input_data, '%m/%d/%y')

    # calculate the changed version:
    number_version_changed = 0
    number_version_changed = (current_version_day - zero_version_day).days + 1

    patch = 0
    minor = 0
    major = 0

    day_minor = 0
    day_major = 0

    for i in range(1, number_version_changed):
        day_minor += 1
        day_major += 1
        patch += 1

        if day_minor % 7 == 0:
            minor += 1
            patch = 0
            # day_minor = 1
        if day_major % 28 == 0:
            major += 1
            minor = 0
            patch = 0
            # day_major = 1

    result = '{}.{}.{}'.format(major, minor, patch)

    return result


def solve(input_data):

    '''Function `solve` dùng để `test`, học viên không cần chỉnh sửa gì thêm
    Chỉ thay đổi lại tên function của mình bên dưới cho phù hợp

    Gía trị trả về của hàm `solve` và `your_function` là như nhau

    :rtype str:
    '''
    result = your_function(input_data)
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    
    return result


def main():
    input_data = None

    # sử dụng `sys.argv` hoặc `argparse` để gán gía trị yêu cầu
    # vào biến `input_data`
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    input_data = sys.argv[1]
    # input_data = "02/03/16"

    logger.debug("Getting version for the day %s", input_data)
    print(input_data, solve(input_data))

    for d in "02/03/16", "09/06/16", "06/23/17":
        print(d, solve(d))


if __name__ == "__main__":
    main()
