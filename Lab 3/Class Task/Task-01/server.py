import socket

HEADER=16
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())

#bind the address
ADDR=(SERVER, PORT) #binding IP and port
FORMAT="utf8"
DISCONNECT_MSG="End"

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # (ipv4, TCP)
server.bind(ADDR)



server.listen()
print(f"server is Listening at {ADDR}")

conn, addr= server.accept()
print(f"Connected to{addr}")
connected=True
while connected:
    msg_length=conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length=int(msg_length)
        msg=conn.recv(msg_length).decode(FORMAT)
        print(f"{msg}")
        if not msg==DISCONNECT_MSG:
            # print(f"Server:(Message Received from Client): {msg}")
            conn.send(f"{msg}".encode(FORMAT))
        else:
            connected=False
            conn.send("Disconnected".encode(FORMAT))
        
conn.close()
            