
def find_two_missing_numbers(arr, n):
    lenth = len(arr) + 1

    xor_arr  = 0
    xor_element = 0
    for x in arr:
        xor_arr ^= x

    for i in range(1, lenth):
        xor_element ^= i

    xor_res = xor_arr ^ xor_element
    ab = xor_res & -xor_res
    




















arr = [3, 1, 5, 6]
n  = 6

find_two_missing_numbers(arr , n)
print()