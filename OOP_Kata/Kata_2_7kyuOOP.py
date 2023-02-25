"""https://www.codewars.com/kata/563089b9b7be03472d00002b/train/python"""


class List:
    def remove_(self, integer_list, values_list):
        for i in range(len(integer_list)-1, -1, -1):
            if integer_list[i] in values_list:
                integer_list.remove(integer_list[i])

        return integer_list


lst = List()
print(lst.remove_([1, 1, 2, 3, 1, 2, 3, 4], [1, 3]))