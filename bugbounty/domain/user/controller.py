# from flask import Blueprint, request, make_response, jsonify
from flask_restful import Resource


class UserController(Resource):
    def get(self):
        return {'user': 'user'}

    def post(self):
        pass

# bp = Blueprint('user_bp', __name__)

# @bp.route('/', methods=['POST'])
# def post():
#     if request.method != 'POST':
#         return make_response('Bad Request', 400)
#
#     body = request.get_json(force=True)
#     print(body, request.args, request.json)
#
#     user = User(body['username'], body['email'], body['password'])
#
#     db.session.add(user)
#     db.session.commit()
#
#     print(user)
#
#     return jsonify({'user': user}), 201
#
#
# @bp.route('/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     if request.method == 'GET':
#         user = User.get_by_id(user_id)
#         print(user)
#         if user is not None:
#             return make_response({'user': user}, 200)
#         else:
#             return make_response('', 404)
#     return make_response(405)
