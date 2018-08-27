class Student(object):
    count = 0

    def __init__(self, name, gender, score):
        self.__name = name
        self.__score = score
        self.__gender = gender
        Student.count += 1

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_score(self, score):
        if 0 <= score <= 100:
            return self.__score == score
        else:
            return ValueError('bad score')

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender


bart = Student('Bart Simpson', '男', 88)
print(bart.print_score(), bart.get_gender(), bart.get_grade())
print(dir(bart))
print(Student.count)
lisa = Student('Fizz', '女', 92)
print(Student.count)

