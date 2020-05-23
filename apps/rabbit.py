# -*- coding:utf-8 -*-
from pika import BlockingConnection, URLParameters
from flask import current_app


class RabbitMQ:

    @staticmethod
    def connect():
        credentials = pika.PlainCredentials('guest', 'guest')
        parameters = URLParameters('rabbitmq',
                                   5672,
                                   '/',
                                   credentials
                                    )
        parameters.connection_attempts = 7
        return BlockingConnection(parameters)
