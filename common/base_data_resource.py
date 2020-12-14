from flask_restful import Resource
from flask import Response, request, session
import json
from common.database import BSONtoJSONEncoder


class BaseDataResource(Resource):
    def __init__(self) -> None:
        self.set_organization_id()  # todo: workaround - terrible way of handling context

    def success(self, data):
        """
             handles serialization of the data to json
        """
        return Response(json.dumps({'success' : True, 'data' : data}, cls=BSONtoJSONEncoder),
                        status= 200,
                        mimetype='application/json',
                        content_type='application/json')

    def error(self, data):
        """
             returns 200 status code even if it is error.
             # todo implement error codes
        """
        return Response(json.dumps({'success': False, 'data': data}, cls=BSONtoJSONEncoder),
                        status=200,
                        mimetype='application/json',
                        content_type='application/json')

    def set_organization_id(self):
        """
             sets the organization id into session object to allow lower classes to access user organization context
             this is a workaround for now. should be removed when a context handling implemented.
        """
        organization_id = request.args.get('organization_id')
        try:
            organization_id = int(organization_id)
        except Exception as e:
            organization_id =1
        session['organization_id'] = organization_id
        return organization_id
