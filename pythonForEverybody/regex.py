# Regular Expressions
# https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/regular-expressions
# Regex provides a means of matching text in strings such as certain words or characters of phrases
# Expressions for parsing strings

# Cheat Sheet - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Cheatsheet

# RegEx in Python
import re

test = 'test string!'
# re.search() can be used like the string find() function
print(re.search('!', test))

# re.search('^String', object)
# this says that if the line starts with 'String' -> like startswith()
if re.search('^test', test):
    print('found')

# Wild card chars
# The dot '.' matches any characters
# The wildcard '*' -> any number of times

print(re.search('^t.*!', test))  # Any line that starts with a t, then followed by any chars, any # of times, ends w/ !

# Fine Tuning matches
# Gets any text that starts with 't' then is proceeded by non-whitespace chars any number of times till it find 't'
print(re.search('^t\S+t', test))  # \S match any non-whitespace char, + -> one or more times, \s -> whitespace



