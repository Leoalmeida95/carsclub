# -*- coding:utf-8 -*-
from pika import BlockingConnection, URLParameters, PlainCredentials


class RabbitMQ:

    @staticmethod
    def connect():
        credentials = PlainCredentials('guest', 'guest')
        parameters = URLParameters('rabbitmq',
                                   5672,
                                   '/',
                                   credentials
                                   )
        parameters.connection_attempts = 7
        return BlockingConnection(parameters)
