# -*- coding: utf-8 -*-

# Python
from os import getenv


class Config:
    SECRET_KEY = getenv('SECRET_KEY') or 'uma string randômica e gigante'
    PORT = int(getenv('PORT', 5000))
    DEBUG = getenv('DEBUG') or False
    MONGODB_HOST = getenv('MONGODB_URI')
    AMQP_URI = getenv('AMQP_URI') or ''
    SIGNUP_QUEUE = getenv('SIGNUP_QUEUE') or 'api-users-signup'
    ENABLE_AMQP = getenv('ENABLE_AMQP') or False


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    TESTING = False
    DEBUG = False


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True


class TestingConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True
    MONGODB_HOST = getenv('MONGODB_URI_TEST')
    ENABLE_AMQP = False


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
