from socket import *
import time
import json

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8888))
s.listen(5)


def resp_msg():
    response = {
        'response': '',
        'time': time.time(),
        'alert': 'Hello'
    }

    return json.dumps(response).encode('utf-8')


while True:
    client, addr = s.accept()
    print("Получен запрос на соединение от %s" % str(addr))
    json_msg = client.recv(1024).decode('utf-8')
    print(json_msg)
    client.send(resp_msg())

    client.close()
