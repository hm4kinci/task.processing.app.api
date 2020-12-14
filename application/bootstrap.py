from application.project.bootstrap import project_api
from application.task.bootstrap import task_api
from application.member.bootstrap import member_api

blueprints = [
    task_api,
    project_api,
    member_api
]