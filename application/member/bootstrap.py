from flask import Blueprint
from flask_restful import Api

from application.member import MemberResource

member_api = Blueprint(
    name='Members-API',
    import_name=__name__
)

api = Api(member_api)
api.add_resource(MemberResource, '/members')