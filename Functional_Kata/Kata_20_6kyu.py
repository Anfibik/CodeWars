"""DESCRIPTION:
You have a string. The string consists of words. Before words can be an exclamation mark !.
Also some words are marked as one set with square brackets [].
You task is to split the string into separate words and sets.

The set can't be contained in another set.

Input:
String with words (separated by spaces), ! and [].

Output:
Array with separated words and sets.

Examples:

('Buy a !car [!red green !white] [cheap or !new]')  =>  ['Buy', 'a', '!car', '[!red green !white]', '[cheap or !new]']
('!Learning !javascript is [a joy]')                =>  ['!Learning', '!javascript', 'is', '[a joy]']
('[Cats and dogs] are !beautiful and [cute]')       =>  ['[Cats and dogs]', 'are', '!beautiful', 'and', '[cute]']"""


def clever_split(s):
    current_lst = s.split()
    res = []
    for i, w in enumerate(current_lst):
        lst_string = ''
        if ']' not in w and '[' not in w and w != '':
            res.append(w)
        if '[' in w:
            for j, cw in enumerate(current_lst[i::]):
                lst_string += cw + ' '
                if ']' in cw:
                    lst_string = lst_string.rstrip()
                    current_lst[i:i+j+1] = ['']*(j+1)
                    res.append(lst_string)
                    break
    return res

