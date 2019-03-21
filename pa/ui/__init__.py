from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from pa.config import Config

app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager()
login_manager.init_app(app)

bootstrap = Bootstrap()
bootstrap.init_app(app)

from pa.ui import routes
