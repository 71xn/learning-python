# Reading Files
# https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/reading-files

filename = 'test.txt'  # File name as a string
mode = 'r'  # mode is a char r or w indicating read or write

handle = open(filename, mode)  # Returns a handle that can be used to manipulate the file

print(handle)  # Returns an object with filename, mode and encoding properties

# The newline char \n
stuff = "Hello\nWorld!"
print(stuff)

stuff = 'X\nY'
print(stuff)
print(len(stuff))