age = 19

if age < 18:
    print('Not eligible')
elif age > 25:
    print('Can become Mp')
elif age > 60:
    print('Senior Citizen')
else:
    print('Can vote')

# for loop

words = ['Cat', 'Rat', 'bat']
for w in words:
    print(w, len(words))
