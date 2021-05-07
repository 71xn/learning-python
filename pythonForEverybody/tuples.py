# Tuples
# https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/the-tuples-collection
# Tuples are like lists - they have elements which are indexed starting at
# Tuples are immutable- like a string - cannot alter the contents
# They cannot be sorted, appended or reversed

t = tuple()
print(dir(t))

# Tuples are more efficient since python does not have to build tuples to be modifiable, they are more memory
# efficient and have better performance

# Tuples are preferred over lists for temporary variables

(x, y) = (4, 'fred')
print(y)
(a, b) = (99, 98)
print(a)

# Tuples and dictionaries
d = dict()
d['c1'] = 2
d['c3'] = 4
for (k, v) in d.items():  # the items method for a dictionary returns a list of key value tuples
    print(k, v)

tupes = d.items()
print(tupes)

# Comparison
print((0, 1, 2) < (5, 1, 2))

# Sorting -> sorted() function
print(sorted(d.items()))
