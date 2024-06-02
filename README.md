# UDP-Socket-Programming


In this project I created a mini application in Python using UDP socket programming.

Client Side:

User defines a port number and enters a message.
Message is sent to the server, and server's response is printed.
If the server responds with “Port is not allowed to communicate,” the client socket closes and the program terminates.
Server Side:

Receives messages from clients and prints them with the sender's IP address and port.
If the message length is ≥ 4, the server closes its socket and completes the transaction.
Message Handling:

Port 1234:

Messages start with "Permission" and end with a number (e.g., "Permission1111").
If the format is incorrect, responds with "Invalid Message."
Valid numbers are added to a list and the client is notified with "Permission Accepted."
If the number is already in the list, responds with "Already Permitted."
Port 3333:

Messages start with "Request" and end with a number (e.g., "Request1111").
If the format is incorrect, responds with "Invalid Message."
If the number is in the allowed list, responds with "Request Accepted."
If not, responds with "Request Rejected."
Other Ports:

Responds with "Port not allowed to communicate."
This project demonstrates basic UDP socket communication with message validation and handling based on port numbers.
