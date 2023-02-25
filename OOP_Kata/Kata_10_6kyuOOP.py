"""https://www.codewars.com/kata/5e882048999e6c0023412908/train/python"""


class DefaultList():
    def __init__(self, def_lst, def_vol):
        self.def_lst = def_lst
        self.def_vol = def_vol

    def __getitem__(self, item):
        if len(self.def_lst) <= item:
            return self.def_vol
        return self.def_lst[item]

    def extend(self, ex_list):
        self.def_lst.extend(ex_list)

    def append(self, ex_vol_list):
        self.def_lst.append(ex_vol_list)

    def remove(self, rem_vol_list):
        self.def_lst.remove(rem_vol_list)

    def insert(self, index, ins_vol_list):
        self.def_lst.insert(index, ins_vol_list)

    def pop(self, pos):
        self.def_lst.pop(pos)