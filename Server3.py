import socket
import sys

host = ""
port = 7891

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(5000)

message = "Hello starshine, the earth says hello"

while 1:
    conn, addr = s.accept()
    print("Connected with", addr[0], "+ ", str(addr[1]))

    data = conn.recv(2048)
    print(data.decode())
    reply = "Okay" + data.decode()
    if not data:
        break
    conn.sendall(message.encode())

conn.close()
s.close()