# 利用map函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# -*- coding: utf-8 -*-
from functools import reduce


def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    return reduce(lambda x, y: x * y, L)


print(prod([3, 5, 7, 9]))
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2sum(s):
    return DIGITS[s]


def str2float(s):
    i = s.split('.')
    print(i[0], i[1], i[0]+i[1])
    return reduce(lambda x, y: x * 10 + y, map(char2sum, i[0]+i[1]))/pow(10, len(i[1]))


print(str2float('123.456'))
