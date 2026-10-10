##imports
import socket


##defs
LOCALHOST = '127.0.0.1'
PORT = 8080
network_tuple = (LOCALHOST, PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


##Socket/Server specifications
server.bind(network_tuple)
server.listen()
print("Waiting for connection ...")
client_socket_info, client_socket_ip_port = server.accept()
print(f"Client has connetcet! Socket information: {client_socket_info} Network Information {client_socket_ip_port}")
client_ip, client_port = client_socket_ip_port
# print(f"Client IP: {client_ip} Client Port: {client_port}")


##Client comunication
###Get
client_msg = client_socket_info.recv(1024)
print(client_msg)
print(client_msg.decode())
###Post
client_post_01 = "HTTP/1.1 200 OK\r\n"
client_post_02 = "Content-Type: text/plain\r\n"
client_post_03 = "Content-Length: 12\r\n\r\n"
client_post_04 = "Hello World!"
full_client_post = str(client_post_01 + client_post_02 + client_post_03 + client_post_04)
bytes_client_post = full_client_post.encode()
client_socket_info.sendall(bytes_client_post)



##debug
print(server)
