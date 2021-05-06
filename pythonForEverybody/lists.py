# Lists
# https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/python-lists
# A list is a collection that allows lots of values to be stores under a single variable
# Lists can be any python object

print([1, 24, 76])
print(['red', 'yellow', 'green'])
print(['red', 24, 76])

for i in [5, 4, 3, 2, 1, 'blastoff']:
    print(i)

friends = ['bob1', 'bob2', 'bob3']
for friend in friends:
    print(friend)

z = friends
for x in z:
    print(x)

# Looking inside lists
print(friends[1])  # bob2

# Lists are mutable Strings are not mutable - 'immutable' we cannot change their contents directly, to alter we need
# to make a new string object, Lists are mutable, we csn change any item at a given index

try:
    fruit = 'banana'
    fruit[0] = 'b'
except TypeError:
    print('String are immutable')

# We can change the contents of a list very easily
lotto = [2, 14, 67, 84, 56]
print(lotto)
lotto[2] = 28
print(lotto)

# We can get the length of a list using the len operator

print(len(lotto))

# The range function returns a list of integers that range from 0 -> n-1 for range(n)
r = range(5)

print(r)

# range is very useful for for loops
for i in range(5):
    print(i)

# List operations
# lists can be combined using the + operator
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
c = a + b
print(c)

# Lists can be sliced using the same syntax as for strings
print(c[1:3])
print(c[:4])
print(c[:3])
print(c[:])

# List methods
x = list()
print(type(x))  # Prints the object type and its attributes
print(dir(x))  # Prints all available methods for a certain object

# Building lists
stuff = list()
stuff.append('book')  # items can be added using the append method
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)  # items stay in the same order that they were added

# Checking if something is inside a list
some = [1, 2, 3, 4, 5, 67, 45]
print(0 in some)  # false
print(5 in some)  # true
print(999 not in some)  # true

# Sorting lists
friendsList = friends + ['zoe', 'dave', 'bert']
friendsList.sort()
print(friendsList)

# Built in functions
nums = [2, 43, 65, 67, 444, 23, 1, 7]
print(len(nums))  # Length
print(max(nums))  # Max value in list
print(min(nums))  # Min value in list
print(sum(nums))  # Sum of all numbers in list
print(sum(nums) / len(nums))  # Average -> sum / number of elements

# Average calc
total = 0
count = 0
while True:
    inp = input('Enter a number, type d when done: ')
    if inp == 'd':
        break
    else:
        value = float(inp)
        total += value
        count += 1

avg = total / count
print('Average: ', avg)
