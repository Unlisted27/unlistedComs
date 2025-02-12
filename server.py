import socket
import threading

# Load config from the file
#with open("./config.txt") as file:
    #for line in file:
        #if line.startswith("target_ip:"):
            #target_ip = line.split(":")[1].strip()
        #if line.startswith("target_port:"):
            #target_port = int(line.split(":")[1].strip())
# Server setup
import socket

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = (s.getsockname()[0])
        s.close()
        return ip
    except Exception as e:
        exit(f"Unable to determine IP {e}")
    finally:
        soc.settimeout(None)  # Reset timeout for future use
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#local_ip = get_local_ip()
local_ip = "127.0.0.1"
print(f"Starting server on {local_ip}")
soc.bind((local_ip, 5000))
soc.listen(5)
print("Server listening on port 5000...")

clients = []  # To keep track of all connected clients

def handle_client(conn, addr):
    """Handles communication with a single client."""
    print(f"New connection from {addr}")
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:  # Client disconnected
                break
            print(f"[{addr}] {msg}")
            # Forward the message to all clients except the sender
            for client in clients:
                #if client != conn:  # Don't send the message back to the sender
                try:
                    client.send(msg.encode())
                except Exception as e:
                    print(f"Error forwarding message to {client.getpeername()}: {e}")
        except Exception as e:
            print(f"Error with client {addr}: {e}")
            break

    # Client disconnected, clean up
    print(f"Client {addr} disconnected.")
    clients.remove(conn)
    conn.close()

def accept_connections():
    """Accept new incoming client connections."""
    while True:
        conn, addr = soc.accept()
        clients.append(conn)
        print(f"New client connected: {addr}")
        # Start a new thread to handle this client
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

# Start the thread to accept connections
threading.Thread(target=accept_connections, daemon=True).start()

# Keep the main thread alive
while True:
    pass
