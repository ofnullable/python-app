import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful import Api

from bugbounty.database import db
from bugbounty.env.config import config_by_env

ENV = os.getenv('APP_ENV') or 'dev'
bcrypt = Bcrypt()


def create_app():
    # create and configure the bugbounty
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_by_env[ENV])

    db.init_app(app)

    api = Api(app)

    with app.app_context():

        from bugbounty.domain.program.controller import ProgramController, ProgramListController
        from bugbounty.domain.user.controller import UserController

        # if ENV == 'dev':
        db.drop_all()
        db.create_all()

        api.add_resource(ProgramController, '/program', '/program/<int:id>')
        api.add_resource(ProgramListController, '/programs')
        api.add_resource(UserController, '/user')

        return app
