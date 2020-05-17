# -*- coding: utf-8 -*-

# Third
from flask import redirect
from flask_restful import Api, Resource
from apps.users.resources import SignUp, Activate
from apps.users.resources_admin import AdminUserPageList, AdminUserResource


class Inital(Resource):
    def get(self):
        return redirect("/api", code=302)


class Index(Resource):
    def get(self):
        return {'site': 'Cars Club'}, 200


api = Api()


def configure_api(app):
    api.add_resource(Inital, '/')
    api.add_resource(Index, '/api')
    api.add_resource(SignUp, '/api/users')
    api.add_resource(Activate, '/api/users/activate/<string:user_id>')
    api.add_resource(AdminUserPageList, '/api/admin/users/page/<int:page_id>')
    api.add_resource(AdminUserResource, '/api/admin/users/<string:user_id>')
    api.init_app(app)
