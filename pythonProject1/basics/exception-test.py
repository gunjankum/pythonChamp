try:
    print(x)
except:
    print("Wrong")

try:
    print("Hello")
except:
    print("Something is wrong")
else:
    print("Nothing is wrong")

try:
    print(x)
except:
    print("Something is worng")
finally:
    print("Nothing is wrong")

try:
    f = open("demo.txt")
    try:
        f.write("Ola ola")
    except:
        print("Unable to write")
    finally:
        f.close()
except:
    print("Cant open the file")

abcd = "Hello"
if not type(abcd) is int:
    raise TypeError("Only Int allowed")


num = -1

if num < 0:
    raise Exception("No num below Zero")
