a = "Hello world "
print(a[0])

for x in a:
    print(x)

print(len(a))

print("Hello" in a)
if "Hello" in a:
    print("Its Hello")

if "ola" not in a:
    print("Not In")

str1 = "I love India"

print(str1[0:4])
print(str1[:5])
print(str1[2:])
print(str1[-5:-1])
print(str1.strip())
print(str1.replace('I', 'J'))

srt = "Hello, World"
print(srt.split(","))

age = 35
print(f"Hi my age is {age}")
print(srt.count('o'))
print(srt.find("W"))

lst = [1, 2, 3, 4]
print(lst[1])

thelst = list((1, 2, 3, 4))
print(thelst[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(":::::::::::::::::::::::::::::")
print(len(thislist))

thislist[1:3] = ["alu", "gobhi"]
print(thislist)
thislist.insert(0, "pyaj")
print(thislist)

mylist = ["apple", "banana", "cherry"]
mylist[1:4] = ["mango"]
print(mylist)

mylist.append("banana")
print(mylist)

lst1 = [1, 2, 3, 4]
lst2 = [5, 6, 7, 8]
lst1.extend(lst2)
print(lst1)

lst1.remove(1)
print(lst1)
lst1.pop(2)
print(lst1)
lst1.pop()
print(lst1)

del lst1[0]
print(lst1)

lst1.clear()
print(lst1)

list3 = ["apple", "banana", "cherry"]

for i in range(len(list3)):
    print(list3[i])

[print(x) for x in list3]

newList = [x for x in list3 if 'a' in x]
print(newList)

newList2 = [x for x in range(10) if x < 5]
print(newList2)

hiList = []
for x in range(10):
    hiList.append(x)

print(hiList)
list3.sort(reverse=True)
print(list3)

list4 = ["banana", "Orange", "Kiwi", "cherry"]
list4.sort(key=str.lower)
print(list4)
list4.reverse()
print(list4)

list5 = ["apple", "banana", "cherry"]
list6 = list5.copy()
print(list6)

list7 = ["nome", "Kome"]

list8 = list5 + list7
print(list8)

list9 = [1, 2, 3, 4]
list10 = [5, 6, 7, 8]
list9.extend(list10)
print(list9)

# Tuple

myTup1 = (1, 2, 3, 4)
print(myTup1)

myTup2 = (6,)

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "Kiwi"
x = tuple(y)
print(x)

z = ("Orange",)
x = x + z
print(x)

a = list(x)
a.remove("Orange")
x = tuple(a)
print(x)

# assign variable to elements of a tuple
fruits = ("apple", "banana", "cherry")

(a, b, c) = fruits

print(b)

fruits1 = ("apple", "banana", "cherry")

(a, *b) = fruits1
print(b)

for x in range(len(fruits1)):
    print(fruits1[x])

i = 0

while i < len(fruits1):
    print(fruits1[i])
    i += 1

myTup1 = fruits1 * 3
print(myTup1)

fruit_count = myTup1.count("apple")
print(fruit_count)

# SET

myset = {"apple", "banana", "cherry"}
print(type(myset))
print(myset)

print("apple" in myset)

myset.add("kiwi")
print(myset)

myset2 = {"mango"}

myset.update(myset2)
print(myset)

lst9 = [1]

myset.update(lst9)
print(myset)

myset.remove("kiwi")
print(myset)

myset.discard("cherry")
print(myset)

myset.pop()
print(myset)

# myset.clear() del myset

myset1 = {1,2,3,4}
myset2 = {"a", "b", "c"}
myset3 = myset1.union(myset2)
print(myset3)


e = {"apple", "banana", "cherry"}
f = {"google", "microsoft", "apple"}

#e.intersection_update(f)

z = e.intersection(f)
print(z)

# e.symmetric_difference_update(f)

l = e.symmetric_difference(f)
print(l)

# Dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(thisdict["brand"])

myDict = {"id" : 1, "address": ["city","PIN","Street"]}

print(myDict)
print(myDict["address"])


myDict1= dict(name="Gunjan",age=2,country="India")
print(type(myDict1))

brand = thisdict.get("brand")
print(brand)

abc = thisdict.keys()
print(abc)

thisdict["color"] = "White"
print(abc)
print(thisdict.get("color"))
print(thisdict["color"])
print(thisdict.keys())

bcd = thisdict.values()
print(bcd)

print(thisdict.items())

thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict1.update({"year": 2000})
print(thisdict1)


# thisdict1.pop("year")
# thisdict1.popitem()
print(thisdict1)

# del thisdict1["brand"]

for x in thisdict1:
    print(x)

for x in thisdict1:
    print(thisdict1[x])

for x in thisdict1.values():
    print(x)

for x,y in thisdict1.items():
    print(x, y)

myDict2 = thisdict1.copy()
print(myDict2)


##############################################

ab = 10

if ab < 18:
    print("cant vote")
else:
    print("Can vote")

num1 = 100
num2 = 200
num3 = 300

if num1 < num2 < num3:
    print("Both Cond are true")

if not num2 > num1:
    print("non greater")

if num1 == num2:
    pass

i = 1

while i < 5:
    print(i)
    i += 1
else:
    print("no longer less than 5")

while i < 10:
    print(i)
    if i == 3:
        break
    i += 1













