from flask import request, make_response
from flask_restful import Resource, abort

from .model import Program


class ProgramController(Resource):
    def get(self, id):
        program = Program.get_by_id(id)

        if not program:
            return abort(404)
        return {'program': program}

    def post(self):
        program = request.get_json(force=True)
        saved = Program.create(title=program['title'], contents=program['contents'])

        # Why must do this...
        res = make_response(saved.to_json(), 201)
        res.headers['Content-Type'] = 'application/json'
        return res


class ProgramListController(Resource):
    def get(self, ):
        pass
