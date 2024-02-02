lst = [1, 2, 3, 4]
print(lst)

for x in lst:
    print(x)

lsst = list((1, 2, 3, 4))

print(lsst[0])
print(lsst[-2])

if 1 in lsst:
    print('Yahoo 1')

lsst[0] = 10
print(lsst)

lsst[1:2] = [100, 200]
print(lsst)

lsst[1:3] = [1000]
print(lsst)

lsst.insert(0, 2000)
print(lsst)

lsst.append(900)
print(lsst)

# append list or any other iterable

num = [1, 2, 3, 4, 5]
num1 = [6, 7, 7, 8, 9]
num.extend(num1)
print(num)

num.remove(1)
print(num)

num.pop(0)
print(num)

num.pop()
print(num)

del num[0]
print(num)

# num.clear()

print(len(num))

# Looping Using List Comprehension

[print(x) for x in num]

new_num = [x for x in num]
print(new_num)

new_list = [x for x in range(10)]
print(new_list)

my_list = ['apple', 'banana']
my_new_list = [x.upper() for x in my_list]
print(my_new_list)

num3 = [9, 6, 8, 1, 4]

num3.sort()
print(num3)

num3.sort(reverse=True)

print(num3)

num3.reverse()
print(num3)

# copy list

lst1 = [1, 2, 3, 4]
lst2 = lst1.copy()

lst3 = list(lst1)

# Tuples

tup1 = (1, 2, 3, 4)
print(type(tup1))

# crate a tuple with one item

tup2 = (1,)

tup3 = tuple((1, 2, 3, 4))

tup4 = (10,)

tup3 += tup4

# set

set1 = {1, 2, 3, 3, 4}
print(set1)

# iterate

for x in set1:
    print(x)

print(1 in set1)

set1.add(5)

print(set1)

set2 = {6, 7, 8, 9}

set1.update(set2)

# add any iterable to a set with update


set1.remove(1)
print(set1)

set1.discard(2)
print(set1)

# set1.clear() , del set1


print(set1)

set3 = {1, 2, 3, 4}
set4 = {5, 6, 7, 8}

set5 = set3.union(set4)

set3.update(set4)

set6 = {1, 2, 3, 4}
set7 = {4, 5, 6, 7}
# set6.intersection_update(set7)
set6.symmetric_difference_update(set7)
print(set6)

# set8 = set6.intersection(set6)
set8 = set6.symmetric_difference(set7)
print(set8)

# Dictionary

dict1 = {"name": "Gunjan",
         "age": 21,
         "job": "Engineer"}
print(dict1)


# The dict() Constructor
dict2 = dict(name="Coco", age=4)
print(dict2)


#  Accessing Items

print(dict2["name"])
print(dict2["age"])
print(dict2.get("name"))
print(dict2.keys())

# Add new item

dict2["color"] = "Fair"
print(dict2.keys())

print(dict2.values())

dict2["name"]= "Advait"
print(dict2.values())

print(dict2.items())

# If

if "name" in dict2:
    print("Name is Coco")

# Change items

dict2.update({"name": "Advait Narayan"})
print(dict2)

dict2.pop("age")
print(dict2)
dict2.popitem()
print(dict2)

dict3 = {"car" : "Maruti", "Model": "Zen"}
del dict3["Model"]
print(dict3)


dict3.clear()
print(dict3)

# Loop Dict

dict4 = {"name": "Gunjan", "age": 21, "comp": "ayla"}

for x in dict4.keys():
    print(x)

for x in dict4.values():
    print(x)

for x, y in dict4.items():
    print(x, y)

dict5 = dict4.copy()
print(dict5)

dict6 = dict(dict5)
print(dict6)


