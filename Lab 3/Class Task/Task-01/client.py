import socket

HEADER=16
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())

#bind the address
ADDR=(SERVER, PORT) #binding IP and port
FORMAT="utf8"
DISCONNECT_MSG="End"

#Only change here
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # (ipv4, TCP)
client.connect(ADDR)

def send(msg):    
    message = msg.encode(FORMAT)
    msg_length = len(message) 
    send_length = str(msg_length).encode(FORMAT)
    send_length+=b' '*(HEADER-len(send_length)) #finding the remaining length
    
    #! Sending the length of the message
    client.send(send_length)
    #! Sending the message
    client.send(message)
    #* Message received from the server
    received_msg = client.recv(2048).decode(FORMAT)
    print(f"Client (Received msg from Server): {received_msg}")    
#write your code here   

#! Sending the IP Address and Device name of the client
send(f"Client's IP Address is {SERVER} and Client's Device name is {socket.gethostname()}")
