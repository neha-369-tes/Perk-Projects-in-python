import socket
import threading

# List to keep track of connected clients
clients = []

def broadcast(message, sender_socket):
    """
    Sends a message to all clients except the sender.
    """
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"Received: {message.decode('utf-8')}")
                broadcast(message, client_socket)
            else:
                client_socket.close()
                clients.remove(client_socket)
                break
        except Exception as e:
            print(f"Error: {e}")
            client_socket.close()
            clients.remove(client_socket)
            break

def start_server():
    """
    Sets up the server to accept incoming client connections.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # Bind to all interfaces on port 12345
    server_socket.listen(5)
    print("Server started on port 12345. Waiting for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_server()
