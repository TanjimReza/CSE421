import platform
import subprocess
import time

def run_server():

    print(f"""---- Starting server... ----
    Python version: {platform.python_version()}
    Running Command: python server_thread.py
    """)
    time.sleep(2)
    try:
        subprocess.Popen('start cmd /k python -c "from server_thread import start; start()"', shell=True)
    except Exception as e:
        print(f"Error: {e}")
    print("----Server Started----")

def run_multiple_clients(client_number=3):
    print(f"""---- Starting {client_number} clients...
    """)
    try: 
        for i in range(client_number):
            print(f"""Starting client {i+1}...""")
            subprocess.Popen('start cmd /k python -c "from client import client_start; client_start()"', shell=True)
            time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
    print("Multiple Clients Started")

print("----Starting Server and Multiple Clients----")
client_number = int(input("Enter number of clients to start (default=3): ") or 3)
if client_number:
    print(f"Starting {client_number} clients...")
else:
    print("Starting 3 clients...")
run_server()    
run_multiple_clients(client_number) 
print("----Server and Multiple Clients Started----")
time.sleep(5)