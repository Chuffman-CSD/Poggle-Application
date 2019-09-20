#!/usr/bin/python3
#Chris Huffman
#9/20/19

import socket
import sys

host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host,port))
except socket.error as e:
    print (str(e))
s.listen(5)

def threaded_client(conn):
    conn.send(str.endcode('welcome, type a message'))

    while True:
        data = conn.recv(2048)
        reply = 'Server Output: ' + data.decode('t-f8')
        
