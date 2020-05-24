# -*- coding:utf-8 -*-
from pika import BlockingConnection, URLParameters
from os import getenv


class RabbitMQ:

    @staticmethod
    def connect():
        # credentials = PlainCredentials('guest', 'guest')
        parameters = URLParameters(getenv('AMQP_URI'))
        parameters.connection_attempts = 7
        return BlockingConnection(parameters)
