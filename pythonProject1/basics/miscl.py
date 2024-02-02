import datetime
import math
import json
import re

x = datetime.datetime.now()
print(x.strftime("%A"))

y = min(1, 2, 3)
print(y)
z = max(10, 20, 200)
print(z)

a = math.ceil(1.1)
print(a)
b = math.floor(1.2)
print(b)

jstr = '{"Name" : "Gunjan" , "age": "21","city": "BLR"}'

jstr1 = json.loads(jstr)
print(jstr1)

str1 = {"name": "coco",
        "age": "3",
        "city": "BLR"}

strj = json.dumps(str1)
print(strj)

txt = "The rain in Spain"
abc = re.search("^The.*Spain$", txt)
if abc:
    print("We have a match")
else:
    print("Naaaa")
