from flask import jsonify
from app.DB import db
from app.DB.Models import User, UserInfo
from werkzeug.security import generate_password_hash
from flask_jwt_extended import set_access_cookies, create_access_token


def AddUser(email, password, yandex_token, client):
    try:
        if db.session.query(User).filter_by(email=email).first() or db.session.query(User).filter_by(yandex_token=yandex_token).first():
            return jsonify({"error": "User already exists"}), 400
        new_user = User(email = email, password = generate_password_hash(password), yandex_token = yandex_token)
        db.session.add(new_user)
        db.session.flush()
        new_user_info = UserInfo(user_id = new_user.user_id, login = client.me.account.login,first_name = client.me.account.first_name,second_name = client.me.account.second_name)
        db.session.add(new_user_info)
        access_token = create_access_token(identity=str(new_user.user_id))
        resp = jsonify({'login': True})
        resp.status_code = 200
        set_access_cookies(resp, access_token)
        db.session.commit()
        return resp
    except Exception as e:
        return jsonify({"error" : f"Error on server: {e}"}), 500


def VerifyUser(email, password):
    try:
        user = db.session.query(User).filter_by(email=email).first()
        if not user or not user.check_password(password=password):
            return jsonify({"message": "Wrong password or email"}), 401
        print(user.user_id)
        access_token = create_access_token(identity=str(user.user_id))
        resp = jsonify({'login': True})
        resp.status_code = 200
        set_access_cookies(resp, access_token)
        return resp
    except Exception as e:
        return jsonify({"error" : f"Error on server: {e}"}), 500