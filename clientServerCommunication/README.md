# Python Socket Chat Application

A simple multithreaded client-server chat application using Python's built-in `socket` and `threading` libraries. This project demonstrates how to build a basic network communication system where multiple clients can connect to a central server and exchange messages in real time.

## 🧠 Features

* Server accepts multiple client connections
* Clients can send and receive messages
* Messages are broadcast to all connected clients (except the sender)
* Clean handling of client disconnection and error

## 🖥️ Server Setup

The server listens for incoming client connections on port `12345`. Once a client connects, a new thread is created to handle communication with that client.

## 👥 Client Setup

Each client connects to the server and runs a thread to continuously receive messages. The client can send messages or type `exit` to disconnect.

## 🚀 Getting Started

1. **Run the server**

   ```bash
   python server.py
   ```
2. **Run one or more clients** (in separate terminals):

   ```bash
   python client.py
   ```

## 🔧 Requirements

* Python 3.x

No external libraries are needed; everything uses Python's standard library.

## 📌 Notes

* Make sure the server is started before any clients connect.
* Clients and server must be on the same network or accessible via IP for remote communication.

## 💡 Future Improvements

* Add usernames or nicknames for clients
* Encrypt messages for secure communication
* Create a GUI using `tkinter` or other frameworks
