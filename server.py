# Keith Marble
# CS372 Summer 2020
# Project 4
# Server for client/server chat, modified from project 1
# Used this tutorial as a guide: http://zetcode.com/python/socket/

import socket

# Create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Name host
    host = 'localhost'
    port = 52356

    # Bind socket to host/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    print(f"Socket binded to {port}")

    # Start socket listening
    sock.listen()
    conn, addr = sock.accept()
    print("Connected by ", addr)
    print("Waiting for message...")

    # Print response
    res = conn.recv(4096)
    if not res:
        sock.close()

    # Print client message
    print(res.decode())

    # Get user input
    print("Type /q to quit")
    print("Enter message to send...")
    print(">", end="")
    data = input()

    # Check if we quit
    if data == "/q":
        sock.close()

    # Send data
    conn.sendall(data.encode('utf-8'))
    
    with conn:
        while True:
            # Print response
            res = conn.recv(4096)
            if not res:
                break

            # Print client message
            print(res.decode())

            # Get user input
            print(">", end="")
            data = input()

            # Check if we quit
            if data == "/q":
                break

            # Send data
            conn.sendall(data.encode('utf-8'))