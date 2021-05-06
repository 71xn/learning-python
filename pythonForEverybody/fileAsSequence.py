# File Handle as a Sequence

file = open('test.txt')
for line in file:
    print(line)

fhand = open('test.txt')
inp = fhand.read()  # Reads the whole file into a var that can be iterated over etc.

print(len(inp))
for char in inp:
    print(char)

# print(inp[:20])

# Searching through a file w/ continue

file = open('test.txt')
for line in file:
    line = line.rstrip()  # The newline char is considered as whitespace so if we .rstrip() we remove the whitespace
    if not line.startswith('line'):  # If the line it reads does not start with 'line' it is skipped
        continue
    print(line)
