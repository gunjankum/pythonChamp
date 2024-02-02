# List

list1 = [1, 2, 3, 4]
print(list1)

for x in list1:
    print(x)
print(list1[1])
print(list1[-1])
print(list1[0:2])
print(list1[-3:-1])

if 1 in list1:
    print("Its there")

list1[0] = 100
print(list1)

list1[1:3] = [200, 300]
print(list1)
list1[1:3] = [100]
print(list1)
list1.insert(0, "Apple")
print(list1)
list1.append("Kumar")
print(list1)
lst2 = [10, 20, 20]
list1.extend(lst2)

print(list1)
list1.remove("Apple")
print(list1)
list1.pop(0)
print(list1)
list1.pop()
print(list1)

for x in range(len(list1)):
    print(list1[x])

# List Comp

[print(x) for x in list1]

list3 = [1, 2, 3, 4]
sq = [x * x for x in list3]
print(sq)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newList = [x for x in fruits if 'a' in x]
print(newList)

myList = [x for x in range(10) if x < 5]
print(myList)

myNew = ["Banana" for x in fruits]
print(myNew)

numList = [1, 3, 2, 6, 5, 4]
numList.sort()
print(numList)
numList.sort(reverse=True)
print(numList)

numList.reverse()
print(numList)

numList2 = numList.copy()
print(numList2)

numList3 = list(numList2)
print(numList3)

num = numList3.count(1)
print(num)

# Tuples

tup1 = (1, 2)
print(type(tup1))
print(tup1)

for x in tup1:
    print(x)

print(tup1[0])

x = ("apple", "banana", "cherry")
y = list(x)
y.append("Kiwi")
x = tuple(y)
print(x)

z = ("mango",)

x = x + z
print(x)

fruits1 = ("apple", "banana", "cherry")

(a, b, c) = fruits1

print(a)
print(b)
print(c)

fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(d, e, *f) = fruits2
print(d)
print(e)
print(f)

fruits3 = ("apple", "banana", "cherry")
fruits4 = fruits3 * 3
print(fruits4)

# Set

set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(type(set1))

set1.add(4)
print(set1)

set1.update(set2)
print(set1)

set1.remove(1)
print(set1)
set1.discard(2)
print(set1)
set1.pop()
print(set1)

set2 = {1, 2, 3, 4}
set3 = {4, 5, 6}
set4 = set2.union(set3)
print(set4)

set2.update(set4)
print(set2)

# dict

veh = {"brand": "maruti", "make": 1972, "cost": 1000}

for x in veh.values():
    print(x)

mod = veh.get("brand")
print(mod)

print(veh.keys())
print(veh.values())

veh["color"] = "white"

print(veh.keys())
print(veh.values())

print(veh.items())

veh.update({"make": 2001})
print(veh)

veh.pop("brand")
print(veh)
veh.popitem()
print(veh)

for x, y in veh.items():
    print(x, y)

dict2 = veh.copy()
print(dict2.items())


# lambda

def func(n):
    return lambda a: a * n


triple = func(3)
print(triple(11))
