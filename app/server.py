from socket import AF_INET, SOCK_STREAM, socket
import time
import json
import logging
import log.server_log_config

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8888))
s.listen(5)

app_log = logging.getLogger('app')


def create_response_msg():
    response = {
        'response': '',
        'time': time.time(),
        'alert': 'Hello'
    }
    return response


def reform_response_msg():
    return json.dumps(create_response_msg()).encode('utf-8')


def send_server_response():
    client.send(reform_response_msg())


def receive_client_message():
    client_msg = client.recv(1024)
    return client_msg


while True:
    client, addr = s.accept()
    app_log.info("Получен запрос на соединение от %s" % str(addr))
    json_msg = receive_client_message().decode('utf-8')
    print(json_msg)
    send_server_response()

    client.close()
