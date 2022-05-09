"""https://www.codewars.com/kata/624e0a4c3e1d7b0031588666/train/python"""


def recurrence(values):
    nadir_index = values.index(min(values))
    for i in range(nadir_index+1, len(values)-2):
        if values[i-1] < values[i] < values[i+1] < values[i+2]:
            return True
    return False


print(recurrence([7.91, 2.43, 1.49, 0.99, 0.74, 0.48, 0.52, 0.50, 0.66, 1.26, 1.36, 1.35]))
