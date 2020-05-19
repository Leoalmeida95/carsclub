# -*- coding:utf-8 -*-
from json import dumps

from apps.rabbit import RabbitMQ


class ProducerSignUp:

    def __init__(self, queue: str):
        conn = RabbitMQ.connect()
        self.queue = queue
        self.channel = conn.channel()
        self.channel.queue_declare(queue=queue, durable=True)

    def publish(self, user):
        from apps.api import api
        from apps.users.resources import ConfirmEmail
        url = api.url_for(ConfirmEmail, user_id=user.get('id'), external=True)

        context = {"data": user, "url": url}

        message = self.message(name="Cars-Club",
                               to=user.get('email'),
                               **context
                               )

        try:
            body = dumps(message)
        except Exception as e:
            raise e

        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue,
            body=body
        )

    def message(
        self,
        name: str,
        to: str,
        subject: str = 'Confirme o Email',
        ffrom: str = 'no-reply@cars-club.com',
            **kwargs):

        message = {
            'app': name,
            'from': ffrom,
            'to': to,
            'subject': subject,
            'body': '''
            Você se registrou em nossa plataforma {app}.
            Precisamos que ative seu email na seguinte url {url}
            '''
        }

        if kwargs:
            message['context'] = kwargs

        return message
