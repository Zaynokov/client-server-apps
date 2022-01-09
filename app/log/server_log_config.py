import logging

app_log = logging.getLogger('app')
app_log.setLevel(logging.INFO)

file_handler = logging.FileHandler('log/server.log')
file_format = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(message)s')
file_handler.setFormatter(file_format)
file_handler.setLevel(logging.INFO)

app_log.addHandler(file_handler)
