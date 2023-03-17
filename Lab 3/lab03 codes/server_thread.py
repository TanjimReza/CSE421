import socket
import threading
HEADER=16
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())

#bind the address
ADDR=(SERVER, PORT) #binding IP and port
FORMAT="utf8"
DISCONNET_MSG="End"

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # (ipv4, TCP)

server.bind(ADDR)



server.listen()
print(f"server is Listening at {ADDR}")




def handle_clients(conn,addr):
    connected=True
    
    while connected: #client is connected
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length= int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT) # how many length of messages
            if msg==DISCONNET_MSG:
                connected=False
                conn.send("Goodbye".encode(FORMAT))
            else:
                print(msg)
                vowels = "aeiouAEIOU"
                vowel_count = sum([1 for char in msg if char in vowels])
                if vowel_count == 0:
                    conn.send("No vowels in the message".encode(FORMAT))
                elif vowel_count <= 2:
                    conn.send("Enough vowels I guess".encode(FORMAT))
                else: 
                    conn.send("Too many vowels".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print("Server is listening")
    while True:
        conn, addr= server.accept()
        thread=threading.Thread(target=handle_clients,args=(conn,addr))
        thread.start()
        print(f"total Clients connected: {threading.active_count()-1} ")
start()