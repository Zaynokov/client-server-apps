import unittest
from app.client import create_presence_msg, reform_presence_msg, receive_server_message
from app.server import create_response_msg, reform_response_msg, receive_client_message


class ClientTestCase(unittest.TestCase):

    def test_type_presence_msg(self):
        result = create_presence_msg()
        self.assertEqual(type(result), dict, 'Неверный тип данных')

    def test_type_reform_presence_msg(self):
        result = reform_presence_msg()
        self.assertEqual(type(result), bytes, 'Неверный тип данных')

    def test_type_receive_server_message(self):
        result = receive_server_message()
        self.assertEqual(type(result), bytes, 'Неверный тип данных')

    def test_presence_msg(self):
        result = create_presence_msg()
        self.assertEqual(result['action'], 'presence')


class ServerTestCase(unittest.TestCase):

    def test_type_response_msg(self):
        result = create_response_msg()
        self.assertEqual(type(result), dict, 'Неверный тип данных')

    def test_type_reform_response_msg(self):
        result = reform_response_msg()
        self.assertEqual(type(result), bytes, 'Неверный тип данных')

    def test_type_receive_client_message(self):
        result = receive_client_message()
        self.assertEqual(type(result), bytes, 'Неверный тип данных')

    def test_response_msg(self):
        result = create_response_msg()
        self.assertTrue(result.get('response'))
