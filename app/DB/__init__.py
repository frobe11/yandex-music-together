from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    with app.app_context():
        from app.DB import Models

from app.DB.auth_service import AddUser, VerifyUser
__all__ = ['AddUser', 'VerifyUser']
