# 求和函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 不返回结果，返回求和函数
def lazy_num(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum    # 返回的不是结果，是求和函数


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


# 利用闭包返回一个计数器函数，每次调用它返回的递增整数
def createCounter():
    a = [0]

    def counter():
        a[0] += 1
        return a[0]
    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())



