from flask import Blueprint
from flask_restful import Api

from application.project import ProjectResource

project_api = Blueprint(
    name='Project-API',
    import_name=__name__
)

api = Api(project_api)
api.add_resource(ProjectResource, '/projects')