"""https://www.codewars.com/kata/6400aa17431f2d89c07eea75/train/python"""
weights = {
    'R': 25,
    'B': 20,
    'Y': 15,
    'G': 10,
    'W': 5,
    'r': 2.5,
    'b': 2,
    'y': 1.5,
    'g': 1,
    'w': 0.5,
}
#
#
# def barbell_weight(barbell):
#     barbell = barbell.replace("-", " ").split()
#     res = [weights[w] for w in barbell[0]]
#     return sum(res) * 2
#
#
def load_barbell(weight):
    flag = 0
    weight = (weight - 25) / 2
    barbell_one_side = ''
    for key, value in weights.items():
        if flag == 0 and weight < 2.5:
            barbell_one_side = 'c' + barbell_one_side
            flag = 1
        range_value = int(weight // value)
        for i in range(range_value):
            barbell_one_side = key + barbell_one_side

        weight = weight - weight // value * value
        if weight + 5 == 0:
            break
    #

















    
#
# print(load_barbell(70)) #-------crB--------------------Brc-------
