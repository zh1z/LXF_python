# 偏函数
import functools


def int2(x, base=2):
    return int(x, base)


int2 = functools.partial(int, base=2)  # 吧一个函数的某些参数固定住（也就是设置默认值），返回一个新的函数

