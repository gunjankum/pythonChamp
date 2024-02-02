def replace_with_greater_right(arr1):
    num = len(arr1)
    max_right = -1

    for i in range(num - 1, -1, -1):
        current_val = arr1[i]
        arr1[i] = max_right

        max_right = max(current_val, max_right)


arr1 = [16, 17, 4, 3, 5, 2]
arr2 = [6, 2, 4, 5, 3, 1]
replace_with_greater_right(arr1)
print(arr1)
