# 斐波那契数列类实现
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a+b
        return a


for n in Fib():
    print(n)
print('第六个元素为：', Fib()[5])
