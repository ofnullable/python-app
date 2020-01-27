from flask import Flask

from bugbounty.settings import DevConfig
from bugbounty.env.extensions import db, bcrypt, cors, migrate
from bugbounty.domain.user.controller import bp as user_bp
from bugbounty.domain.program.controller import bp as program_bp


def create_app(config=DevConfig):
    # create and configure the bugbounty app
    print('create and configure the bugbounty app', config)
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(config)

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    print('register extensions...')
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.drop_all()
        db.create_all()


def register_blueprints(app):
    print('register blueprints...')
    origins = ['http://localhost:3000']
    cors.init_app(user_bp, origins=origins)
    cors.init_app(program_bp, origins=origins)

    app.register_blueprint(user_bp)
    app.register_blueprint(program_bp)
