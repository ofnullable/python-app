from flask import Flask
from flask_restful import Api

from bugbounty.settings import DevConfig
from bugbounty.env.extensions import db, bcrypt, cors, migrate


def create_app(config=DevConfig):
    # create and configure the bugbounty
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(config)

    db.init_app(app)

    api = Api(app)

    with app.app_context():
        from bugbounty.domain.program.controller import ProgramController, ProgramListController
        from bugbounty.domain.user.controller import UserController

        api.add_resource(ProgramController, '/program', '/program/<int:id>')
        api.add_resource(ProgramListController, '/programs')
        api.add_resource(UserController, '/user')

        return app


def register_extensions(app):
    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
