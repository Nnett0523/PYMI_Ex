#!/usr/bin/env python3


def sumall(*args):
    '''Viết function ``sumall`` tính tổng của tất cả các argument (int, float,
    hoặc string) được gọi. Thay input_data bằng code phù hợp.
    '''
    #https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3
    res = 0
    for arg in args:
        if isinstance(arg, int) or isinstance(arg, float):
            res += arg
        elif isinstance(arg, str):
            res += int(arg.strip())
    return res
def solve():
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp

    result = sumall(1, 2, 3, 4.5, 5, ' 6 ')
    result2 = sumall(1, 2, 3, 4.5, 5, 9, ' 6 ')

    return result, result2


def main():
    print(solve())


if __name__ == "__main__":
    main()
