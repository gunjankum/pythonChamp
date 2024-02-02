
import json


# Python to Json
x = { "name":"Gunjan",
      "age" : 24,
      "salary": 100}

y = json.dumps(x)

print(y)

# Json to python
a = '{"name":"Gunjan","age" : 24,"salary": 100}'

b  = json.loads(a)
print(b["age"])

print(json.dumps(31.76))

str1 = "Hello"


import pickle

myList = [1,2,3,4]

file = open("Impo","wb")
pickle.dump(myList,file)
file.close()


