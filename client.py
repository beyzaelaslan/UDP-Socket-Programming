import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = int(input("Enter port no: "))
client_socket.bind(('localhost', port))


try:
    while True:
        message = input("Enter a message: ")
        client_socket.sendto(message.encode(), ('localhost', 5000))

        response, server_address = client_socket.recvfrom(1024)
        print(response.decode())

        if response.decode() == "Port is not allowed to communicate":
            break
finally:
    client_socket.close()
