# -*- coding: utf-8 -*-

from flask import request

from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist

from apps.responses import resp_ok, resp_exception

from apps.messages import MSG_RESOURCE_FETCHED_PAGINATED

from .models import User
from .schemas import UserSchema


class AdminUserPageList(Resource):

    def get(self, page_id=1):
        schema = UserSchema(many=True)
        page_size = 10

        if 'page_size' in request.args:
            if int(request.args.get('page_size')) < 1:
                page_size = 10
            else:
                page_size = int(request.args.get('page_size'))

        try:

            users = User.objects().paginate(page_id, page_size)

        except FieldDoesNotExist as e:
            return resp_exception('Users', description=e.__str__())

        except Exception as e:
            return resp_exception('Users', description=e.__str__())

        extra = {
            'page': users.page, 'pages': users.pages, 'total': users.total,
            'params': {'page_size': page_size}
        }

        result = schema.dump(users.items)

        return resp_ok(
            'Users', MSG_RESOURCE_FETCHED_PAGINATED.format('usuários'),
            data=result.data, **extra
        )
