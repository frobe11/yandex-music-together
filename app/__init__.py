from flask import Flask
from config import Dev, Prod
import os

app = Flask(__name__)

env = os.getenv("CONFIG", "dev")
app.config.from_object(Dev if env == "dev" else Prod)

from app import routes