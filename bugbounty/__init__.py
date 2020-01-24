from flask import Flask

from bugbounty.env.extensions import db, bcrypt, cors, migrate
from bugbounty.settings import DevConfig


def create_app(config=DevConfig):
    print('create and configure the bugbounty app', config)
    # create and configure the bugbounty
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(config)

    register_extensions(app)

    return app


def register_extensions(app):
    print('register extensions..', app)
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.drop_all()
        db.create_all()
