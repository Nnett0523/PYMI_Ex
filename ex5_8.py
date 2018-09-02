#!/usr/bin/env python3
import string


def solve():

    '''Trả về biểu diễn của 20 mã ASCII từ 33 đến 53 theo format
    [(33, BIEUDIENCUA33), ...]
    Unicode codepoint của các số từ 0->9, a-z, A-Z.
    Unicode codepoint tương ứng với ký tự ``\t`` ``\n``, `` ``

    Gợi ý: dùng ``chr()``, ``ord()``.
    '''
    tabcodepoint = None
    newlinecodepoint = None
    spacecodepoint = None
    twenty_ascii = []
    unicodes = []

    # Xoá dòng raise và Viết code vào đây set các giá trị phù hợp
    tabcodepoint = ord('\t')
    newlinecodepoint = ord('\n')
    spacecodepoint = ord(' ')
    for i in range(33, 53):
        twenty_ascii.append((i, chr(i)))
    for i in range(0, 10):
        unicodes.append(chr(i))
    for letter in string.ascii_letters:
        unicodes.append(ord(letter))

    result = (twenty_ascii, unicodes, tabcodepoint,
              newlinecodepoint,
              spacecodepoint)
    return result


def main():
    for part in solve():
        print(part)
        if isinstance(part, list):
            for elem in part:
                print(elem)


if __name__ == "__main__":
    main()
