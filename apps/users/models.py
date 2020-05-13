# Python
from datetime import datetime

# Third
from mongoengine import (
    BooleanField,
    IntField,
    DateTimeField,
    EmailField,
    EmbeddedDocument,
    EmbeddedDocumentField,
    StringField
)

# Apps
from apps.db import db

TYPES = ('Disel', 'Etanol', 'Gasolina', 'GNV')


class Fuel(EmbeddedDocument):
    Nome = StringField(max_length=8, choices=TYPES)


class Car(EmbeddedDocument):
    """
    Default implementation for cars fields
    """
    color = StringField(default='')
    value = IntField(default=0)
    mileage = IntField(default='')
    number_ports = IntField(default=2)
    fuel = EmbeddedDocumentField(Fuel, default=Fuel)


class Roles(EmbeddedDocument):
    """
    Roles permissions
    """
    admin = BooleanField(default=False)


class UserMixin(db.Document):
    """
    Default implementation for User fields
    """
    meta = {
        'abstract': True,
        'ordering': ['email']
    }

    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    roles = EmbeddedDocumentField(Roles, default=Roles)
    created = DateTimeField(default=datetime.now)
    active = BooleanField(default=False)

    def is_active(self):
        return self.active

    def is_admin(self):
        return self.roles.admin


class User(UserMixin):
    '''
    Users are Buyers
    '''
    meta = {'collection': 'users'}

    full_name = StringField(required=True)
    cpf_cnpj = StringField(default='')
    cars = EmbeddedDocumentField(Car, default=Car)
