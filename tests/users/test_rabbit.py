from apps.rabbit import RabbitMQ
from pika import BlockingConnection


def test_rabbitmq_must_have_connection_method():
    assert hasattr(RabbitMQ, 'connect')


def test_rabbitmq_connection_be_callable():
    connect = getattr(RabbitMQ, 'connect')
    assert hasattr(connect, '__call__')


def test_rabbitmq_must_return_blocking_connection():
    result = RabbitMQ.connect()
    assert isinstance(result, BlockingConnection)
