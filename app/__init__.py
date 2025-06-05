from flask import Flask
from config import Dev, Prod
from app.DB import db, init_app
from flask_jwt_extended import JWTManager

import os

app = Flask(__name__)
env = os.getenv("CONFIG", "dev")
app.config.from_object(Dev if env == "dev" else Prod)

jwt = JWTManager(app=app)

db.init_app(app)
init_app(app)

from app.routesAPI import auth_bp
app.register_blueprint(auth_bp)