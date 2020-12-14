from flask import request
from processing import (TaskProcessor, TaskLinker)
from common.base_data_resource import BaseDataResource
from application.project import ProjectRepository
from application.member import MemberRepository
from flask_cors import cross_origin


class Process(BaseDataResource):
    def __init__(self) -> None:
        super().__init__()

    @cross_origin()
    def get(self):
        text_input = request.args.get('body')
        if text_input is None or len(text_input) < 10:
            return self.error('task must be at least 10 character length')

        project_repository = ProjectRepository()
        member_repository = MemberRepository()

        task_processor = TaskProcessor()
        task_processing_result = task_processor.process(text_input=text_input)
        task_linker = TaskLinker()
        task_linker.register_repository('project', project_repository)
        task_linker.register_repository('member', member_repository)
        task_linking_result = task_linker.process(task_processing_result=task_processing_result)

        combined_output = dict()
        combined_output['corrected_input'] = task_processing_result.corrected_text
        combined_output['dates'] = task_processing_result.dates
        combined_output['type'] = task_processing_result.contact_type
        combined_output['contact_persons'] = task_linking_result.contact_persons
        combined_output['projects'] = task_linking_result.projects

        return self.success(combined_output)

