"""https://www.codewars.com/kata/541c8630095125aba6000c00/train/python"""


def digital_root(n):
    while n > 10:
        n = sum(map(int, str(n)))
    return n


print(digital_root(493193))