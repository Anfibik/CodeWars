"""https://www.codewars.com/kata/56311e4fdd811616810000ce/train/python"""


class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        return list({i: "".join(str(i) for i in integers_list).count(str(i)) for i in digits_list}.items())



l = List()
integers_list = [1, 1, 2, 3, 1, 2, 3, 4]
digits_list = [1, 3]

print(l.count_spec_digits(integers_list, digits_list))