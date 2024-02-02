def find_anagram(str1, str2):

    if len(str1) != len(str2):
        return False

    res = 0

    for x in str1+str2:
        res ^= ord(x)

    return res == 0


str1 = "abcd"
str2 = "dcba"
result = find_anagram(str1, str2)
print(result)
