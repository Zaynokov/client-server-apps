from socket import AF_INET, SOCK_STREAM, socket
import time
import json
import logging
import log.client_log_config

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))

app_log = logging.getLogger('app')


def logger(func):
    def call(*args, **kwargs):
        app_log.info(f"{time.time()} Функция {func.__name__} вызвана из функции main")
        return None
    return call


@logger
def create_presence_msg():
    message = {
        'action': 'presence',
        'time': time.time()
    }
    return message


@logger
def reform_presence_msg():
    return json.dumps(create_presence_msg()).encode('utf-8')


@logger
def send_message():
    s.send(reform_presence_msg())


@logger
def receive_server_message():
    server_msg = s.recv(1024)
    return server_msg


def main():
    send_message()
    receive_message = receive_server_message().decode('utf-8')

    app_log.info("Ответ сервера: %s" % receive_message)
    s.close()


if __name__ == '__main__':
    main()
