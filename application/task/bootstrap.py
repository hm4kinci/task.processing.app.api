from flask import Blueprint
from flask_restful import Api

from application.task import Process

task_api = Blueprint(
    name='Task API',
    import_name=__name__
)

api = Api(task_api)
api.add_resource(Process, '/tasks/process')
