import os

from bugbounty import create_app
from bugbounty.settings import config_by_env

ENV = os.getenv('APP_ENV') or 'dev'
app = create_app(config_by_env[ENV])

if __name__ == '__main__':
    app.run(host='0.0.0.0')
