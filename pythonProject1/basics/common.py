x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

a = b = c = 10
print(a)
print(b)
print(c)

# unpack

str = ['a', 'b', 'c']
s1, s2, s3 = str
print(s1)
print(s2)
print(s3)

car = 'maruti'
for x in car:
    print(x)

print('m' in car)
print(len(car))

if 'm' in car:
    print("m is there")
if 'n' not in car:
    print('n is not there')


hell = 'Hello, World! '
print(hell.strip())
print(hell.lower())
print(hell.upper())
print(hell.replace('H', 'J'))
print(hell.split(','))

age = 10
company = 'Ayla'
txt = 'Hello my age is {} and i work for {}'
print(txt.format(age,company))

