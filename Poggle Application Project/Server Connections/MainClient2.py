# Import socket module 
import socket
from PoggleServer import *
  
  
def Main(): 
    # local host IP '127.0.0.1' 
    host = '127.0.0.1'
  
    # Define the port on which you want to connect 
    port = 12345
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    # connect to server on local computer 
    s.connect((host,port)) 
  
    # message you send to server 
    message = "CSD Class"
    while True: 
  
        # message sent to server 
        s.send(message.encode('ascii')) 
  
        # message received from server 
        data = s.recv(1024)
        print(data)
  
        # print the received message 
        # here it would be a reverse of sent message 
        print("Received from the server",message)
        
        def Test():
            # ask the client whether they want to continue
            x = 0
            while x == 0:
                ans = input('\nDo you want to continue(y/n) :') .lower()
                if ans == 'y':
                    x = 1
                    print("\n=-=Send a message, Q// or q// to quit=-=\n")
                    username = input("Enter a username: ")
                    i = 0
                    while i == 0:
                        data = s.recv(1024)
                        print("\n")
                        ui_main = input("Username_here: ").capitalize()
                        if ui_main == ("Q//") or ui_main == ("q//"):
                            i = 1
                            print("Quitting..")
                            s.close()
                            print("Goodbye!")
                            quit()
                        else:
                            #u_message = msg
                            m_msg = ui_main
                            l_msg = "\n" + username+": " + m_msg +"\n"
                            Messages.append(l_msg)
                            #test
                            #print(data,"This is a test")
                            test = l_msg
                            s.send(test.encode('utf-8'))
                            data = s.recv(1024)
                            print(test)
                elif ans == 'n':
                    a = 1
                    print("Pressed n")
                    s.close()
                    print("Goodbye!")
                    quit()
                else:
                    print("\nEnter [y] or [n]")
                
        Test()
                    
        #else: 
            #break
    # close the connection 
    s.close() 
  
if __name__ == '__main__': 
    Main() 
