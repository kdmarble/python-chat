A simple chat application that connects a client to a server via an IPv4 TCP socket.

To start, use command "python3 server.py" to initiate the server, bind the socket, and begin waiting for a connection and message.
![Image of server.py](server.png)

To connect to the server, use command "python3 client.py". You'll be prompted to enter a message, or enter "/q" to quit. 
![Image of client.py](client.png)

After hitting enter, the message will be sent to the server, and chatting can commence.