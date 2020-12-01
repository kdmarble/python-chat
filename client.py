# Keith Marble
# CS372 Summer 2020
# Project 4
# Client for client/server chat, modified from project 1
# Used this tutorial as a guide: http://zetcode.com/python/socket/

import socket

# Create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Name host
    host = 'localhost'
    port = 52356

    # Connect
    sock.connect((host, port))
    
    # Get user input
    print("Type /q to quit")
    print("Enter message to send...")
    print(">", end="")
    data = input()

    # Check if we quit
    if data == "/q":
        sock.close()

    # Send data
    sock.sendall(data.encode('utf-8'))
    
    while True:
        # Print response
        res = sock.recv(4096)
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
        sock.sendall(data.encode('utf-8'))
