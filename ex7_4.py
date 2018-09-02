#!/usr/bin/env python3


def solve(text):
    '''Thực hiện biến đổi

      input: [a, abbbccccdddd, xxyyyxyyx]
      output: [a, abb3cc4dd4, xx2yy3xyy2x]

    Giải thích: Những chữ cái không lặp lại thì output giữ nguyên chữ cái đó.
    Những chữ cái liên tiếp sẽ in ra 2 lần + số lần lặp lại liên tiếp.

    Đây là một biến thể của một thuật toán nén dữ liệu có tên Run-length
    encoding (RLE).
    '''
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    result = ''
    text += '\n'  # them de tranh mat thang d
    if len(text) < 2:
        result = text
    else:
        temp = text[0]  # a
        count = 1       # a : 1
        for char in text[1:]:  # bbbccccdddd
            if char != temp:    # d != c
                if count == 1:  # a
                    result += temp  # a
                    temp = char     # b
                    # continue
                elif count > 1:
                    result += temp*2 + str(count)  # a + bb3 + cc4
                    temp = char # d
                    count = 1   # d:1
            else:   # d4
                count += 1
            
    return result


def main():
    print(solve('xxyyyxyyx'))


if __name__ == "__main__":
    main()
