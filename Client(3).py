import socket
import sys

#create TCP socket sock_stream designates it as a a TCP socket as opposed to UDP
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except (socket.error):
    print("An error occurred when creating the socket")
    print("Error code", str(socket.error))

    sys.exit(0)

print("Socket created")

host = "www.google.com"
port = 7891


remote_ip = "157.230.131.10"


print("Ip address of host", host, " is: ", remote_ip)

s.connect((remote_ip, port))

print("Socket connected to ", host, " with port ", port, " on IP address: " , remote_ip)

message = "the Eagle has landed"

try:
    s.sendall(message.encode()) #"was expecting bytes, got str instead" found .encode() on https://stackoverflow.com/questions/40139775/python-3-socket-programming-using-sendall-vs-sendto?noredirect=1
except:
    print("Sending the message failed")

print("We sent some info to the page")


rec = s.recv(1024)

print(rec.decode())

#s.close()
print("Socket closed")