import socket


MAX_CLIENTS = 4
PERMISSION_PORT = 1234
REQUEST_PORT = 3333

permitted_numbers = []


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 5000))

client_count = 0
client_addresses = []

try:
    while client_count < MAX_CLIENTS:

        message, client_address = server_socket.recvfrom(1024)
        message = message.decode()

        print(f"Message: {message}")
        print(f"Client Address:  {client_address}")

        if client_address not in client_addresses:
            client_addresses.append(client_address)
            client_count += 1

        if client_address[1] == PERMISSION_PORT:
            if message.lower().startswith("permission") and message[len("Permission"):].isdigit():
                number = int(message[len("Permission"):])
                if number in permitted_numbers:
                    server_socket.sendto(b"Already Permitted", client_address)
                else:
                    permitted_numbers.append(number)
                    server_socket.sendto(b"Permission Accepted", client_address)
            else:
                server_socket.sendto(b"Invalid Message", client_address)
        elif client_address[1] == REQUEST_PORT:
            if message.lower().startswith("request") and message[len("Request"):].isdigit():
                number = int(message[len("Request"):])
                if number in permitted_numbers:
                    server_socket.sendto(b"Request Accepted", client_address)
                else:
                    server_socket.sendto(b"Request Rejected", client_address)
            else:
                server_socket.sendto(b"Invalid Message", client_address)
        else:
            server_socket.sendto(b"Port is not allowed to communicate", client_address)


finally:
    server_socket.close()
    print(f"The number of connected clients is: {client_count}")
