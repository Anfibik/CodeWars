"""https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python"""


def solution(s):
    return [s[i:i+2].ljust(2, '_') for i in range(0, len(s), 2)]



