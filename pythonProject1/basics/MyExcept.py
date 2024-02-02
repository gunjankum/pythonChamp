
try:
    print(x)
except:
    print("Wrong")
else:
    print("Nothing is wrong")

try:
    print(y)
except:
    print("Wrong")
finally:
    print("Run Always")

# RaISE

x = -1

if not type(x) is int:
    raise Exception("Negative Number")

username= input("Enter Name")
print(username)


num = 10

print(f"Price of TV is {num}")






