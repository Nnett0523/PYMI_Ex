#!/usr/bin/env python3

import csv
import os
import time


def find_max_price(datafile):
    f = open(datafile)
    dr = csv.DictReader(f, ['time', 'price', 'UNKNOWN']) # NOQA
    # Viết tiếp code vào đây

    try:
        # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
        lst = []
        for row in dr:
            lst.append(row)

        lst_time = []
        lst_price = []
        for row in lst:
            lst_time.append(row['time'])
            lst_price.append(row['price'])

        lst_price = list(map(float, lst_price))
        lst_time = list(map(float, lst_time))

        max_price = max(lst_price)
        max_time = int(lst_time[lst_price.index(max_price)])
        
        max_time = time.strftime('%Y-%m-%d', time.gmtime(max_time))

    finally:
        f.close()

    return max_time, max_price


def solve():
    '''Tìm ngày giá BTC lên cao nhất. Trả về Tuple chứa ngày ở định dạng
    YYYY-mm-dd (VD: 2017-06-19) và giá VND của 1 BTC
    '''
    # http://api.bitcoincharts.com/v1/csv/
    datafile = 'localbtcVND.csv'
    exdir = os.path.dirname(__file__)
    datapath = os.path.join(exdir, datafile)

    result = find_max_price(datapath)
    return result


def main():
    now = time.gmtime(int(time.time()))
    print(now.tm_year, now.tm_mon, now.tm_mday)
    print(solve())


if __name__ == "__main__":
    main()
