import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.env.config import config_by_env

db = SQLAlchemy()
ENV = os.getenv('APP_ENV') or 'dev'


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_by_env[ENV])

    db.init_app(app)

    with app.app_context():
        from app.domain.user import controller as user
        from app.domain.program import controller as program

        db.create_all()

        app.register_blueprint(user.bp, url_prefix='/user')
        app.register_blueprint(program.bp, url_prefix='/program')

        return app
