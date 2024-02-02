'''
A = [1,4,9]

s = ''.join(map(str , A))
print(s)
k = int(s)+ 1
print(k)
'''


def plus_one(A):
    A[-1] = A[-1] + 1  # increment from the last element.
    # traverse the string in reverse order and check for occurrence of 10 and 0
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


A1 = [1, 9, 9, 9]  # regular case
A2 = [9, 9, 9]  # edge case
print(plus_one(A2))
