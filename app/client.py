from socket import *
import time
import json

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))


def presence_msg():
    message = {
        'action': 'presence',
        'time': time.time()
    }

    return json.dumps(message).encode('utf-8')


s.send(presence_msg())

server_msg = s.recv(1024)
s.close()
print("Ответ сервера: %s" % server_msg.decode('utf-8'))
