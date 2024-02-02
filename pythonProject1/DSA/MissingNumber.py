
def find_missing_element(arr):
    n = len(arr) +1
    xor_arr = 0
    for i in range(1, n+1):
        xor_arr ^= i
    xor_element = 0
    for x in arr:
        xor_element ^=x

    missing_element = xor_arr ^ xor_element
    return missing_element


arr = [2,1,3,5,6,4,8]
missing_element = find_missing_element(arr)
print(missing_element)



