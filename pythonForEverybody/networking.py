# Networking
# https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/networking-with-python

# Python has built in support for TCP sockets using the socket library

import socket
# mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mySock.connect('google.com', 80)  # IP/URL, Port Number

# Requests over HTTP are made using the GET command, and data is sent using the POST command

# Writing a web browser in python
mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(('data.pr4e.org', 80))  # IP/URL, Port Number
request = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()  # HTTP encoding our web request
mySock.send(request)

while True:
    data = mySock.recv(512)  # We receive the data in 512 byte chunks
    if len(data) < 1:  # Checks if the data stream is over -> exits loop -> closes connection
        break
    print(data.decode())
mySock.close()

# Encoding -> Most Webpages and sites use UTF-8 Encoding -> 1-4 bytes, compatible with
# ASCII (American Standard Code for Information Interchange)
