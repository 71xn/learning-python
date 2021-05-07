# Dictionaries
# https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/python-dictionaries
# A collection of values each with their own key identifiers - like a java hashmap

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
ddd['age'] = 27
print(ddd)

# Literals
jjj = {'name': 'bob', 'age': 21}
print(jjj)

# Counting occurrences
ccc = dict()
ccc['count1'] = 1
ccc['count2'] = 1
print(ccc)
ccc['count1'] = ccc['count1'] + 1
print(ccc)

# Counting names ex.
counts = dict()
names = ['bob', 'bob6', 'bob4', 'bob2', 'bob', 'bob6']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)

# The get method
if name in counts:
    x = counts[name]
else:
    x = 0

# get returns the value for a specified key in the dictionary
x = counts.get(name, 0)  # 0 is the default value


# Counting w/ get
counts = dict()
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
