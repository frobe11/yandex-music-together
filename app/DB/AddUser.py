from flask import jsonify
from app.DB import db
from app.DB.Models import get_user_model
from werkzeug.security import generate_password_hash

def AddUser(email, password, yandex_token):
    User = get_user_model()
    print(User)
    try:
        if db.session.query(User).filter_by(email=email).first() or db.session.query(User).filter_by(yandex_token=yandex_token).first():
            return jsonify({"error": "User already exists"}), 401
        new_user = User(email = email, password = generate_password_hash(password), yandex_token = yandex_token)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User is created"}), 200
    except Exception as e:
        return jsonify({"error" : f"Error on server: {e}"}), 500
