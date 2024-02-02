class MyClass:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

    def my_func(self):
        print("Helly my name is " + self.name)


p1 = MyClass("Gunjan", 21)

print(p1.name, p1.age)

p1.my_func()


print(p1)
