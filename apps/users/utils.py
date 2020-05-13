# -*- coding: utf-8

from mongoengine.errors import (
                                FieldDoesNotExist,
                                DoesNotExist,
                                MultipleObjectsReturned
                            )
from .models import User
from apps.responses import (
    resp_does_not_exist,
    resp_exception
)


def check_password_in_signup(password, confirm_password):
    if not password:
        return False

    if not confirm_password:
        return False

    if not password == confirm_password:
        return False

    return True


def get_user_by_id(user_id: str):
    try:

        return User.objects.get(id=user_id)

    except DoesNotExist as e:
        return resp_does_not_exist('Users', 'Usuário')

    except FieldDoesNotExist as e:
        return resp_exception('Users', description=e.__str__())

    except Exception as e:
        return resp_exception('Users', description=e.__str__())


def exists_email_in_users(email: str, instance=None):
    """
    Verifico se existe um usuário com aquele email
    """
    user = None

    try:
        user = User.objects.get(email=email)

    except DoesNotExist:
        return False

    except MultipleObjectsReturned:
        return True

    # verifico se o id retornado na pesquisa é mesmo
    # da minha instancia informado no parâmetro
    if instance and instance.id == user.id:
        return False

    return True
