from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from app.DB.Models import Base

db = SQLAlchemy()

def init_app(app):
    with app.app_context():
        Base.prepare(db.engine, reflect=True)
        print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])
        
        # Какие таблицы увидел SQLAlchemy?
        print("Tables in Base.classes:", dir(Base.classes))
        if hasattr(Base.classes, 'users'):
            User = Base.classes.users
            print("User model:", type(User))




from app.DB.AddUser import AddUser
__all__ = ['AddUser']
