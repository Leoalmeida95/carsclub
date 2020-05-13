# -*- coding: utf-8 -*-

from flask import request

from flask_restful import Resource
from mongoengine.errors import (
                                FieldDoesNotExist,
                                NotUniqueError,
                                ValidationError
                            )

from apps.responses import (
                            resp_data_invalid,
                            resp_ok,
                            resp_exception,
                            resp_already_exists
                        )

from apps.messages import (
                            MSG_RESOURCE_FETCHED_PAGINATED,
                            MSG_RESOURCE_FETCHED,
                            MSG_NO_DATA,
                            MSG_ALREADY_EXISTS,
                            MSG_INVALID_DATA,
                            MSG_RESOURCE_UPDATED,
                            MSG_RESOURCE_DELETED
                        )

from .models import User
from .schemas import UserSchema, UserUpdateSchema
from .utils import get_user_by_id, exists_email_in_users


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


class AdminUserResource(Resource):

    def get(self, user_id):
        result = None
        schema = UserSchema()

        user = get_user_by_id(user_id)

        if not isinstance(user, User):
            return user

        result = schema.dump(user)

        return resp_ok(
            'Users', MSG_RESOURCE_FETCHED.format('Usuários'),  data=result.data
        )

    def put(self, user_id):
        result = None
        schema = UserSchema()
        update_schema = UserUpdateSchema()
        req_data = request.get_json() or None
        email = None

        if req_data is None:
            return resp_data_invalid('Users', [], msg=MSG_NO_DATA)

        user = get_user_by_id(user_id)

        if not isinstance(user, User):
            return user

        # carrega os dados de acordo com o schema de atualização
        data, errors = update_schema.load(req_data)

        # em caso de erros retorno uma resposta 422 com os erros de
        # validação do schema
        if errors:
            return resp_data_invalid('Users', errors)

        email = data.get('email', None)

        if email and exists_email_in_users(email, user):
            return resp_data_invalid(
                'Users', [{'email': [MSG_ALREADY_EXISTS.format('usuário')]}]
            )

        try:
            # para cada chave dentro do dados do update schema
            # atribuimos seu valor
            for i in data.keys():
                user[i] = data[i]

            user.save()

        except NotUniqueError:
            return resp_already_exists('Users', 'usuário')

        except ValidationError as e:
            return resp_exception(
                                    'Users',
                                    msg=MSG_INVALID_DATA,
                                    description=e.__str__()
                                )

        except Exception as e:
            return resp_exception('Users', description=e.__str__())

        result = schema.dump(user)

        return resp_ok(
            'Users', MSG_RESOURCE_UPDATED.format('Usuário'),  data=result.data
        )

    def delete(self, user_id):
            # Busco o usuário na coleção users pelo seu id
            user = get_user_by_id(user_id)

            # se não for uma instancia do modelo User retorno uma resposta
            # da requisição http do flask
            if not isinstance(user, User):
                return user

            try:
                user.active = False
                user.save()

            except NotUniqueError:
                return resp_already_exists('Users', 'usuário')

            except ValidationError as e:
                return resp_exception(
                                        'Users',
                                        msg=MSG_INVALID_DATA,
                                        description=e.__str__()
                                    )

            except Exception as e:
                return resp_exception('Users', description=e.__str__())

            return resp_ok('Users', MSG_RESOURCE_DELETED.format('Usuário'))
