# -*- coding: utf-8 -*-

# Third
from flask_restful import Api, Resource


# Extendendo de Resource
class Index(Resource):

    def get(self):
        return {'hello': 'world by apps'}

# Instanciando a API do FlaskRestful
api = Api()

def configure_api(app):
    # adicionando a rota '/' a sua classe correspondente Index
    api.add_resource(Index, '/')
    api.init_app(app)
