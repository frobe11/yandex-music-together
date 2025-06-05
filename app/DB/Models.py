from werkzeug.security import check_password_hash
from app.DB import db

class User(db.Model):
    __tablename__ = 'users' 

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False)
    yandex_token = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def check_password(self, password):
        return check_password_hash(self.password, password=password)

    user_info = db.relationship('UserInfo', back_populates='users', uselist=False)

class UserInfo(db.Model):
    __tablename__ = 'user_info'

    info_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    login = db.Column(db.Text)
    first_name = db.Column(db.Text)
    second_name = db.Column(db.Text)

    users = db.relationship('User', back_populates='user_info')