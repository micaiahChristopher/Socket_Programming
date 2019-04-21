import socket
import sys

host = ""
port = 7891

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(5000)

dict = {}

last_message = "thanks for playing, buckaroo"

#message = "Hello starshine, the earth says hello"

while 1:
    conn, addr = s.accept()
    print("Connected with", addr[0], "+ ", str(addr[1]))

    data = conn.recv(2048)
    data_list = data.decode().split(" | ")
    print(data_list)
    dict[data_list[0]] = data_list
    key_list =[]
    new_dict = sorted(dict, key= dict.get, reverse= True)
    print(new_dict)

    for keys in new_dict:
        key_list.append(keys)
    #print(key_list)
    #print(key_list)
    if data_list[0] == key_list[0]:
        message = "Well done! You placed 1st, with a score of " + data_list[0]
    else:
        message = "You did not top the leader-board, better luck next time kiddo."
    if not data:
        break
    conn.sendall(message.encode())
    conn.sendall(last_message.encode())
conn.close()
s.close()