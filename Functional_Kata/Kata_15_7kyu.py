"""https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python"""


def disemvowel(string_):
    return ''.join(i for i in string_ if i.lower() not in 'euioa')



print(disemvowel('AuiUmM(&AIE;Zy loaFA_Oe OdW EE[AEUq\' iEIpmjUEa*O&&O]w#`"}oUuR GzU= iBEOJ}lE[YifrE`ieaeieb'))
print()