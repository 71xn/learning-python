# Intermediate Strings
# https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/intermediate-strings

# Slicing Strings
s = 'Monty Python'

print(s[0:4])  # Outputs 'Mont', 0 -> pos 4 but not including

print(s[6:7])  # Outputs 'P', character 6 up to but not including character 7

print(s[6:20])  # Outputs 'Python' go from char 6 (including) up to pos 20, however < 20 -> end of string
# If second num (x) s[0:x] x > s.length -> goes to end of string

print(s[:2])  # If no stating index specified -> starts at index 0

print(s[8:])  # No end specified, go to end of string

print(s[:])  # No start or end values specified, prints whole String

# Concatenation
# The + operator is used to concatenate strings in python

a = 'Hello'
b = a + 'There'
print(b)

c = a + ' ' + 'There'
print(c)

# in - logical operator
# The in keyword can be used to check if one string is 'in' another string
# The in expression is logical - return True or False, can be used in if else

fruit = 'banana'
print('n' in fruit)  # True
print('m' in fruit)  # False
print('nan' in fruit)  # True

if 'a' in fruit:
    print('Found it!')

# String Comparison
word = 'apple'

if word == 'banana':
    print('True')

# Alphabetical order comparisons
if word < 'banana':
    print(word + ' comes before banana')
elif word > 'banana':
    print(word + ' comes after banana')

# String Library
# These functions are already built into every string
# These functions do not modify the original string, they return a new one

greet = 'Hello Bob'
lower = greet.lower()  # Returns 'hello bob'

print('Hi there'.lower())  # String functions can be called on any string not just one assigned to a var

# Searching Strings
# The find() function -> finds the first occurrence of the substring
# if not found returns -1

fruit = 'banana'
pos = fruit.find('na')
print(pos)  # 2

aa = fruit.find('z')
print(aa)  # -1


# Search and Replace
# Replace function is like a search and replace operator
# Finds substring to be replaced and replaces it with a provided value

greet = 'Hello Bob'
newStr = greet.replace('Bob', 'Jane')  # Format (string to be replaced, string to replace it with)
print(newStr)

newStr = greet.replace('o', 'X')
print(newStr)


# Stripping whitespace
greet = '          Hello Bob    '

print(greet.lstrip())  # Strips the whitespace off of the left side of the string
print(greet.rstrip())  # Strips the whitespace off of the right side of the string

print(greet.strip())  # .strip() removes the whitespace from both sides of the string


# Prefixes

line = 'Please have a nice day'
print(line.startswith('Please'))  # Logical operator, return true if the string starts with given string
print(line.startswith('P'))  # Returns false because the first complete word in the string is not 'P'


# Parsing and extracting

data = 'From flestrange@isa.aberdeen.sch.uk Sat Jun   5  09:14:56 2008'
atPos = data.find('@')
print(atPos)  # 21

spPos = data.find('', atPos)  # Gets sender domain after the @
print(spPos)  # 31

host = data[atPos+1 : spPos]
print(host)  # Prints email domain


# In python 3.7 all strings are in unicode format

word = "bananana"
i = word.find("na")
print(i)
