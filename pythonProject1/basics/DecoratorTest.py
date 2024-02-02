def pretty(func):
    def inner():
        print("i got decorated")
        func()

    return inner


@pretty
def ordinary():
    print("I am ordinary")


ordinary()


# decorated_func = pretty(ordinary)
#
# decorated_func()


def smart_devide(func):
    def inner(a, b):
        print("I am going to divide a and b")
        if b == 0:
            print("Its wrong")
            return
        return func(a, b)

    return inner


@smart_devide
def divide(a, b):
    print(a/b)


divide(4, 2)
divide(2, 0)
