from basics.Person import Person


class Student(Person):

    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.fname, self.lname, "to the class of ", self.graduationyear)


x = Student("Gunjan", "Kumar", 2011)
x.welcome()
