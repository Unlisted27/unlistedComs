import socket
import threading
import os

log = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def receive_messages():
    """ Continuously receives messages from the server. """
    while True:
        try:
            msg = soc.recv(1024).decode()
            if not msg:
                exit("Server disconnected.")
            log.append(msg)
            update_screen()
        except:
            break

def update_screen():
    clear_screen()
    for msg in log:
        print(msg)

# Load config from the file
with open("./config.txt") as file:
    for line in file:
        if line.startswith("target_ip:"):
            target_ip = str(line.split(":")[1].strip())
            print(f"server ip: {target_ip}")
        if line.startswith("target_port:"):
            target_port = int(line.split(":")[1].strip())
            print(f"server port: {target_port}")

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    soc.connect((target_ip, target_port))
except ConnectionRefusedError:
    exit("Connection refused (Hint: Does the server exist?)")
    
# Start the thread to receive messages
threading.Thread(target=receive_messages, daemon=True).start()

# Send messages to the server
while True:
    msg = input("Enter message: ")
    if msg.lower() == "exit":
        soc.send(msg.encode())
        exit("disconnected")
    soc.send(msg.encode())
