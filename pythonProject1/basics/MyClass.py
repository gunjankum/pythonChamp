class MyClass:
#     x = 10
#
#
# p = MyClass()
# print(p.x)


    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return f"{self.name}{self.age}"

    def myFunc(self):
        print("Hello my name is " + self.name)


p1 = MyClass("Gunjan", 25)
print(p1)
p1.myFunc()

class MyChild(MyClass):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def welcome(self):
        print("Welcome", self.name, self.age, self.salary)

p3 = MyChild("Kumar" ,32 ,100)
p3.welcome()


