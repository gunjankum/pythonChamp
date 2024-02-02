a = 10
b = 20

if a > b:
    print("a is greater")
elif a == b:
    print("a equals b")
else:
    print("a less than b")

if a < b: print("a is greater than b")

print("A") if a < b else print("B")

print("A") if a > b else print("=") if a == b else print("B")


num1 = 100
num2 = 200
num3 = 300

if num3 > num2 and num2 > num1:
    print("True")

if num1 == 200 or num2 < 300:
    print("Or")

if not num1 == 1000:
    print("Not Test")

if num1 > num2:
    pass


# While

i = 0

while i < 10:
    print(i)
    i += 1

j = 0

while j < 10:
    print(j)
    if j == 5:
        break
    j += 1

k = 0

while k < 10:
    k += 1

    if k == 5:
        continue
    print(k)


# For

for x in range(10):
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)


for x in range(3):
    print(x)
else:
    print("Loop Finished")

for x in range(5):
    if x == 3:
        break
    print(x)
else:
    print("Not Finished Yeah !!")




