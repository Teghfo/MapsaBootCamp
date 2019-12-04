import socket
import time
import select

IP = ''
PORT = 8210

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((IP, PORT))

server_socket.listen(10)

socket_list = [server_socket]

clients = {}


while True:
    read_socket, write_socket, exception_socket = select.select(
        socket_list, [], socket_list)
    for s in read_socket:
        if s == server_socket:
            client_socket, address = server_socket.accept()

            if client_socket:
                client_socket.send(bytes("welcome!", 'utf-8'))
                socket_list.append(client_socket)
                user = address[0]
                clients[client_socket] = user
                print("Connection Established from {}".format(address))
        else:
            message = s.recv(1024)
            if not message:
                socket_list.remove(s)
                del clients[s]
                continue
            print(message.decode('utf-8'))
            for client_socket in clients:
                if client_socket != s:
                    fullText = clients[s] + ' says ' + message.decode('utf-8')
                    client_socket.send(bytes(fullText, 'utf-8'))
    for s in exception_socket:
        socket_list.remove(s)
        del clients[s]
    print(socket_list)
# server_socket.close()
