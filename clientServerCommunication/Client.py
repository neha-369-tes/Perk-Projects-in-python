import socket
import threading
import sys

def receive_messages(client_socket):
    """
    Listens for incoming messages from the server and displays them.
    """
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                client_socket.close()
                break
        except:
            client_socket.close()
            break

def start_client():
    """
    Connects to the chat server and handles user input.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))  # Connect to the server's IP and port

    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        message = input()
        if message.lower() == 'exit':
            client_socket.close()
            break
        else:
            try:
                client_socket.send(message.encode('utf-8'))
            except:
                client_socket.close()
                break

if __name__ == "__main__":
    start_client()
