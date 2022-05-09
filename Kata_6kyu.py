"""https://www.codewars.com/kata/58539230879867a8cd00011c/train/python"""


def find_children(dancing_brigade):
    parents = sorted(filter(lambda p: p.isupper(), dancing_brigade))
    children = sorted(filter(lambda p: p.islower(), dancing_brigade))
    res = []
    for p in parents:
        res.append(p)
        for c in children:
            if p == c.upper():
                res.append(c)
    return ''.join(res)
