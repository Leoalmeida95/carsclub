# -*- coding: utf-8 -*-

from marshmallow import Schema
from marshmallow.fields import Email, Str, Boolean, Nested, Int
from apps.messages import MSG_FIELD_REQUIRED


class UserRegistrationSchema(Schema):
    id = Str()
    full_name = Str(required=True, error_messages={
        'required': MSG_FIELD_REQUIRED})
    email = Email(required=True, error_messages={
        'required': MSG_FIELD_REQUIRED})
    password = Str(required=True, error_messages={
        'required': MSG_FIELD_REQUIRED})


class UserSchema(Schema):
    id = Str()
    full_name = Str(required=True, error_messages={
        'required': MSG_FIELD_REQUIRED})
    email = Email(required=True, error_messages={
        'required': MSG_FIELD_REQUIRED})
    cpf_cnpj = Str()
    active = Boolean()


class FuelSchema(Schema):
    Nome = Str()


class CarSchema(Schema):
    color = Str()
    value = Int()
    mileage = Int()
    number_ports = Int()
    fuel = Nested(FuelSchema)


class UserUpdateSchema(Schema):
    full_name = Str()
    email = Email()
    cpf_cnpj = Str()
    cars = Nested(CarSchema)
    active = Boolean()
