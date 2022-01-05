from socket import AF_INET, SOCK_STREAM, socket
import time
import json

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))


def create_presence_msg():
    message = {
        'action': 'presence',
        'time': time.time()
    }
    return message


def reform_presence_msg():
    return json.dumps(create_presence_msg()).encode('utf-8')


def send_message():
    s.send(reform_presence_msg())


def receive_server_message():
    server_msg = s.recv(1024)
    return server_msg


send_message()
print("Ответ сервера: %s" % receive_server_message().decode('utf-8'))
s.close()
