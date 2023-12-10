str = ('hello '
       'world')
print(str)

word = 'Python'
print(word[0])
print(word[5])
print(word[-1])
print(word[-2])
print(word[-6])
print(word[0:2])
print(word[2:5])
print(word[:2])
print(word[4:])
print(word[-2:])

squares = [1, 4, 9, 16, 25]
print(squares)


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)
letters.append('A')
print(letters)
print(len(letters))

