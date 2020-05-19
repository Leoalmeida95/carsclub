# -*- coding:utf-8 -*-
from pika import BlockingConnection, URLParameters
from flask import current_app


class RabbitMQ:

    @staticmethod
    def connect():
        parameters = URLParameters(current_app.config.get('AMQP_URI'))
        parameters.connection_attempts = 7
        return BlockingConnection(parameters)
