"""https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python"""


def top_3_words(text):
    symbol = "!\"#$%&()*+,./:;<=>?@[\]^_`{|}~-"
    for i in text:
        if i in symbol:
            text = text.replace(i, " ")
    text = text.lower().split()
    text = [i for i in text if i.replace("'", "").isalpha()]
    amount_symbol = {}
    for i in set(text):
        amount_symbol[i] = text.count(i)
    list_d = list(amount_symbol.items())
    list_d.sort(key=lambda i: i[1], reverse=True)
    return [i[0] for i in list_d][0:3]





