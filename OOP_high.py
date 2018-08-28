from types import MethodType


class Student(object):
    __slots__ = ('name', 'age')  # 限制class的属性为3个，仅对当前类有用，子类并不继承

    @property
    def score(self):  # 相当于setter方法
        return self._score

    @score.setter
    def score(self, value):  # 相当于getter方法
        if not isinstance(value, int):
            raise ValueError('score must be integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value


s = Student()
s.name = 'Michael'


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


# s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法，仅该实例可调用
# s.set_age(25)

'''
def set_score(self, score):
    self.score = score


Student.set_score = set_score  # 给class绑定方法，这样所有实例均可调用
'''


class Screen(object):
    @property  # 把width变成一个属性
    def width(self):
        return self._width  # 加单下划线避免和属性名重复

    @width.setter
    def width(self, value):
         self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width*self._height

# 测试


s = Screen()
s.width = 1024
s.height = 768
print('resolution = ', s.resolution)
if s.resolution == 786432:
    print('测试通过！')
else:
    print('测试失败！')
