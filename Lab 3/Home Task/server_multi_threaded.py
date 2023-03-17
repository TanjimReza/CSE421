import socket
import threading
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

print(f"Server is Listening at {ADDR}")

"""
4. Create a basic client server program where the server takes the number of hours a person worked from the client and calculates the person's salary.
If the hours worked is less than or equal to 40, then the person receives Tk 200 per hour.
If the hours worked is greater than 40, then the person receives Tk 8000 plus Tk 300 for each hour worked over 40 hours.
The client will provide how many hours the person worked to the server and the server will calculate the salary and send it to the client.

"""
def calculate_salary(hours):
    if hours <= 40:
        salary = hours * 200
        return salary
    else:
        salary = 8000 + (hours - 40) * 300
        return salary



def handle_clients(conn,addr):
    connected=True
    while connected: #* client is connected
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length= int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT) # how many length of messages
            if msg==DISCONNECT_MSG:
                connected=False
                conn.send("Goodbye".encode(FORMAT))
            else:
                salary = calculate_salary(int(msg))
                conn.send(f"Your salary is {salary}".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print("Server is listening")
    while True:
        conn, addr= server.accept()
        thread=threading.Thread(target=handle_clients,args=(conn,addr))
        thread.start()
        print(f"Total Clients connected: {threading.active_count()-1} ")
start()