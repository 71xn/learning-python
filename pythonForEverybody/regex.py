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

# Matching and Extracting Data
# re.search() -> boolean
# re.findall() -> returns list of matching strings

# Finding Numbers
x = 'My favorite 2 numbers are 13 and 56'
y = re.findall('[0-9]+',
               x)  # [] -> denotes a character class, characters in the range wil be selected, + -> one or more
print(y)  # ['2', '13', '56']

# Extracting Strings
y = re.findall('[AEIOIUaeiou]+',  # This will match uppercase or lowercase vowels
               x)
print(y)

# Greedy matching
x = 'From: using the : character'
y = re.findall('^F.+:', x)  # Because there are two possibilities we get back the larger of the two
print(y)  # ['From: using the :']

# Non-Greedy Matching -> '?'
x = 'From: using the : character'
y = re.findall('^F.+?:' ,x)  # Adding the '?' means that we get the first match it finds
print(y)

# Fine Tuning Extraction
email = 'From finn.lestrange@mail.com Sat Jun 5 2021'
y = re.findall('\S+@\S+' ,email)  # Match non-whitespace followed by, match @ followed by, match non-whitespace
print(y)  # ['finn.lestrange@mail.com']

# Matching vs. Extracting Strings
# by using () instead of [] we can tell it to extract if we match a certain condition
# Parenthesis () are not part of the match -> they tell where to start and stop the extraction
y = re.findall('From (\S+@\S+)', email)
print(y)  # Returns ['finn.lestrange@mail.com'] only if the From is present

# ------------------------
# Practical RegEx Examples
# ------------------------

line = 'From finn.lestrange@mail.com Sat Jun 5 2021'

# Getting Email domain v1
y = re.findall('@([^ ]*)', email)
# Looks through the string until it finds an @ symbol -> match any non-blank char [^ ] -> * match any of them
print(y)  # ['mail.com']

# Getting Email domain v2
y = re.findall('^From .*@([^ ]*)' ,line)
# Start at beginning ^ -> look for 'From'
# ' ' see a space
# .* see any number of characters
# see an @
# ([^ ]*) -> start extracting any non-blank as many times until reaches blank
print(y)  # ['mail.com']

# Escape Chars
# Escapable chars like $ need to be prefixed by a \
x = 'We just got $10.00 for cookies'
y = re.findall('\$[0-9.]+', x)
# Match '$' -> [0-9.] Extract any char 0-9 or '.' -> * any number of times
print(y)  # ['$10.00']


