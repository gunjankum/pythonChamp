from basics.MyClass import MyClass


class MyChild(MyClass):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def welcome(self):
        print("Welcome", self.name, self.age, self.salary)

p3 = MyChild("Kumar" ,32 ,100)
p3.welcome()
