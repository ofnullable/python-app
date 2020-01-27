class Config:
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'superimportantsecretkeyvalue'
    SESSION_COOKIE_NAME = 'bb_session'


class DevConfig(Config):
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://developer:1234@192.168.32.30:3306/bugbounty_dev?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'ssmysql+pymysql://developer:1234@192.168.32.30:3306/bugbounty_test?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    DEBUG = False
    TESTING = False


config_by_env = dict(
    dev=DevConfig,
    test=TestConfig,
    prod=ProdConfig
)
