#!/usr/bin/python3
#Chris Huffman
#9/20/19

import socket
import sys

host = '127.0.0.1'
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host,port))
except socket.error as e:
    print (str(e))

def threaded_client(conn):
    conn.send(str.encode('welcome, type a message'))

    while True:
        data = conn.recv(2048)
        reply = 'Server Output: ' + data.decode('t-f8')
        
threaded_client(s)
