# import socket programming library 
import socket
import MainClient1
  
# import thread module 
from _thread import *
import threading 
  
print_lock = threading.Lock()

clients = []
Messages = []
  
# thread fuction 
def threaded(c): 
    while True: 
  
        # data received from client 
        data = c.recv(1024)
        #if not data: 
            #print('Bye') 
              
            # lock released on exit 
            #print_lock.release() 
            #break
  
        # reverse the given string from client 
        #data = data[::-1] 
  
        # send back reversed string to client
        print(data)
        for client in clients:
            client.send(data)
        
  
    # connection closed 
    c.close() 
  
  
def Main():
    host = "127.0.0.1" 
  
    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening")
  
    # a forever loop until client wants to exit 
    for i in range(5):
    #while True:
        messages = []
  
        # establish connection with client 
        c, addr = s.accept()
        clients.append(c)
  
        # lock acquired by client 
        #print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[0]) 
  
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,))
        print("----------Test",addr[0],":",addr[0])
        s.listen(5)
        print("Messages: ",Messages)
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 
