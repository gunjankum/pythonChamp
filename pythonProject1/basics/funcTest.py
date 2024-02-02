def my_func():
    print("My Func")


my_func()


def my_new_func(fname):
    print(fname + " " + "Kumar")


my_new_func("Gunjan")


def my_f1(fname, lname):
    print(fname + " " + lname)


my_f1("Gunjan", "Kumar")


def my_f2(*kids):
    print("my kids name is " + kids[0])


my_f2("coco", "poco", "loco")


def my_f3(kid1, kid2, kid3):
    print("Mu kids name is " + kid3)


my_f3(kid1="coco", kid2="poco", kid3="loco")


def my_f4(**kid):
    print("my kids name is " + kid["lname"])


my_f4(fname="cococ", lname="Narayan")


def my_country(country="Norway"):
    print("i am from " + country)


my_country("India")
my_country("Sweden")
my_country("America")
my_country()


def my_iterable(food):
    for x in food:
        print(x)


fruits = ["Apple", "Banana", "Kiwi"]
my_iterable(fruits)


def my_return(num):
    return num * 10


print(my_return(2))


def my_pass():
    pass


def my_multi(n):
    return lambda a: a * n


doubler = my_multi(2)  # doubler  = lambda a : a * 2
tripler = my_multi(3)

print(doubler(5))
print(doubler(5))
