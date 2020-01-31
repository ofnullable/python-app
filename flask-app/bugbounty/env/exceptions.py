from flask import jsonify

HTTP_STATUS_CODES = {
    'BAD_REQUEST': 400,
    'UNAUTHORIZED': 401,
    'FORBIDDEN': 403,
    'NOT_FOUND': 404,
    'CONFLICT': 409,
    'INTERNAL_SERVER_ERROR': 500
}


class Commons(Exception):
    status_code = HTTP_STATUS_CODES['INTERNAL_SERVER_ERROR']

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = {'message': message}
        self.status_code = status_code if status_code else HTTP_STATUS_CODES['INTERNAL_SERVER_ERROR']

    @classmethod
    def resource_not_found(cls, message):
        return cls(message, HTTP_STATUS_CODES['NOT_FOUND'])

    @classmethod
    def duplicate_key(cls, message):
        return cls(message, HTTP_STATUS_CODES['CONFLICT'])

    def to_json(self):
        rv = self.message
        return jsonify(rv)
