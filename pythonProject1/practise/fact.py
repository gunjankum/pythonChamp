num = int(input("Input the number\n"))
res = 1
def facto(num):
    while num > 0:

        res = res * num
        num = num -1
    return res

print(facto(num))


