# Swap Variables:
x, y = y, x

# Comparision
x = 10
if 10 < x < 20:
    print("True!")


# Generate a List
>>> li = [x*x for x in range(1, 8)]
>>> li
[1, 4, 9, 16, 25, 36, 49]



# Join:
>>> print('\t'.join("HELLO!"))
H       E       L       L       O       !


# Slip a list
>>> li = range(17)
>>> li[::-3]
[16, 13, 10, 7, 4, 1]



# Enumerate
li = 'hello!'
for index, value in enumerate(li, start=5):
    print(index, '--->', value)


  5 ---> h
  6 ---> e
  7 ---> l
  8 ---> l
  9 ---> o
  10 ---> !



# Zip a dict
titles = ['name', 'gender', 'age']
vs1 = ['Harry', 'Male', 26]
di = dict(zip(titles, vs1))
print(di)

{'name': 'Harry', 'gender': 'Male', 'age': 26}


