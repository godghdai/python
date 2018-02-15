class Student():
    # 类变量，不是实例变量
    # 相当于类的静态属性
    test = 'petter petter'

    # 构造函数　必需 return None
    def __init__(self, name, age):
        # 实例变量
        self.name = name
        self.age = age
        # 私有属性
        self.__score = 0
        print('__init__ 1', Student.test)
        print('__init__ 2', self.__class__.test)

    # 实例方法　第一个参数必需有self　
    # self名字可以自定义
    def do_homework(self):
        print('name:'+self.name)
        print('age:'+str(self.age))

    # python 没有public private关键字
    # 默认为public,方法前+__为private
    def __do_other(self):
        pass

    # 类方法 cls名字可以自定义
    @classmethod
    def plus_sum(cls):
        cls.test += "dddd"
        print(cls.test)

    # 跟C#的静态方法不一样
    @staticmethod
    def add(x, y):
        print(Student.test)
        print("this is a static method")


# 不需要new
student = Student('xiaoxiao', 333)
#　先查找实例上的name属性，找不到再查找类变量name
print(student.name)
# {'name': 'abc', 'age': 333}
print(student.__dict__)
print(Student.__dict__)
print(Student.test)
print(student.test)

# python中实例可以调用类的方法
# 但不建意这么做
# student.plus_sum()

# student.add()
# Student.add()


student1 = Student('student1', 333)
# 读取不了__开头的私有属性
# print(student1.__score)
student2 = Student('student2', 333)
# 动态增加了__score的属性，不是原有的
student2.__score = 100
#{'name': 'student2', 'age': 333, '_Student__score': 0, '__score': 100}
# _Student__score 为私有变量
print(student2.__dict__)
print(student2.__score)
#　实际没有私有变量，间接读取私有变量
print(student2._Student__score)


# 继承
class Human():
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('human say')


class Worker(Human):
    def __init__(self, work, name, age):
        self.work = work
        # Human.__init__(self,name,age)
        super(Worker, self).__init__(name, age)

    def say(self):
        super(Worker, self).say()
        print('worker say')


worker = Worker('coder', 'work1', 18)
print(worker.name)
print(worker.work)

worker.say()
