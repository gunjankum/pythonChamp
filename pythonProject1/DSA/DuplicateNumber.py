def finddup(arr):
    xor_arr = 0
    xor_all = 0
    length = len(arr)

    for x in arr:
        xor_arr ^= x
    for y in range(length):
        xor_all ^= y
    res = xor_arr ^ xor_all

    return res


arr = [1, 2, 3, 4, 4, 5]
dup = finddup(arr)
print(dup)
