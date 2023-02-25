"""https://www.codewars.com/kata/571d2e9eeed4a150d30011e7/train/python"""


def scoreboard(who_ate_what):
    current_lst_dicts = []
    for dct in who_ate_what:
        my_dict = {'name': 0, "chickenwings": 0, "hamburgers": 0, "hotdogs": 0}
        my_dict.update(dct)
        current_lst_dicts.append(my_dict)
    res = []
    for dct in current_lst_dicts:
        keys = list(dct.values())
        score_sum = keys[1]*5 + keys[2]*3 + keys[3]*2
        res.append({'name': keys[0], 'score': score_sum})

    return sorted(res, key=lambda key: (-key['score'], key['name']))
