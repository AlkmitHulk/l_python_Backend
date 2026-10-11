##imports
import socket


##defs
LOCALHOST = '127.0.0.1'
PORT = 8080
network_tuple = (LOCALHOST, PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def client_answer_HTTP(content, type_nr, type_msg, socket_info):
    bytes_content = content.encode()

    client_post_01 = f"HTTP/1.1 {type_nr} {type_msg}\r\n"
    client_post_02 = "Content-Type: text/plain\r\n"
    client_post_03 = f"Content-Length: {len(bytes_content) + 1}\r\n"
    client_post_04 = "Connection: close \r\n\r\n"
    client_post_05 = f"{content}\n"
    dec_client_post = client_post_01 + client_post_02 + client_post_03 + client_post_04 + client_post_05 
    bytes_client_post = dec_client_post.encode()
    socket_info.sendall(bytes_client_post)


##Socket/Server specifications    
server.bind(network_tuple)
server.listen()
try:
    while True:
        print("Waiting for connection ...")
        client_socket_info, client_socket_ip_port = server.accept()
        #print(f"Client has connetcet! Socket information: {client_socket_info} Network Information {client_socket_ip_port}")
        client_ip, client_port = client_socket_ip_port
# print(f"Client IP: {client_ip} Client Port: {client_port}")


##Client comunication
###Get
        client_msg = client_socket_info.recv(1024)
        #print(client_msg)
        dec_client_msg = client_msg.decode()
        #print(dec_client_msg)
        
#### Splitten der  der Client MSG
        split_line_filter_msg = "\r\n"
        split_line_msg = client_msg.split(split_line_filter_msg.encode())
        line_01_msg = split_line_msg[0]
        dec_line_01_msg = line_01_msg.decode()
        split_mpc_msg = dec_line_01_msg.split(" ")
        method_msg, path_msg, content_msg = split_mpc_msg
        print(f"Method:{method_msg} and Path: {path_msg}")

####Prüfen und Antworten der Client MSG
        if path_msg == "/":
            client_answer_HTTP("Startseite", "200", "OK", client_socket_info)
        elif path_msg == "/Hallo":
            client_answer_HTTP("Hallo Max!", "200", "OK", client_socket_info)
        else:
            client_answer_HTTP("Seite nicht gefunden", "404", "Not Found", client_socket_info)



        


###Post


##Closing all the Sockets
        client_socket_info.close()
except KeyboardInterrupt:
    print("Admin Closed the Session")
finally:
    server.close()
