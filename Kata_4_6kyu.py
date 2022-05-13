"""https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python"""


def find_outlier(integers):
    res = list(map(lambda x: x % 2, integers))
    if sum(res) > 1:
        return integers[res.index(0)]
    else:
        return integers[res.index(1)]


print(find_outlier( [3372961, 2786271, 495487, 2768827, -4071333, -7690815, 4131867, 3382543, 4757425, -7876226, -4854815, 294577, -7618421, 4957503]))