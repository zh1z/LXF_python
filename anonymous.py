# 匿名函数
def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))

# 用匿名函数lambda

M = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)
print('改造后:', M)
