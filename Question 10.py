# Write a simple client-server program:
#  The server should listen for incoming connections and send a message Hello from
# server!
#  The client should connect to the server and receive the message.
#  Include basic error handling for network operations.

import socket

HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Non-privileged port

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            conn.sendall(b"Hello from server!")
except socket.error as e:
    print(f"Server error: {e}")