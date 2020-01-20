# Import socket module 
import socket, time		 

# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = 12345				

# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 

# receive data from the server 
while True:
    print (s.recv(1024).decode())
    time.sleep(1)