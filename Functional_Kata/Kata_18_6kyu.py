"""https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python"""


def duplicate_count(text):
    res = 0
    text = text.lower()
    for letter in set(text):
        if text.count(letter) > 1:
            res += 1

    return res


