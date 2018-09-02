#!/usr/bin/env python3


def chunk_a_list(iterable, N):
    # Sửa tên, set giá trị return
    temp = []
    res = []
    while len(iterable) > N - 1:
        #tai sao la N -1, boi vi den khi day cac element ra het, neu vua du thi k noi, neu thua ra thi loai phan tu do di.
        temp.append(iterable.pop(0))
        if len(temp) == N:
            res.append(tuple(temp))
            temp = []
    return res



def solve(iterable, N):
    ''' Chia input_data thành các tuple chứa N phần tử (chunk a list).
    Nếu tuple cuối không đủ phần tử thì bỏ đi.
    '''
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp


    # sửa thành tên function phù hợp
    result = chunk_a_list(iterable, N)

    return result


def main():
    li = ['meo', 'bo', 'ga', 'cho', 'chim', 'gau', 'voi']
    print(solve(li, 2))


if __name__ == "__main__":
    main()
