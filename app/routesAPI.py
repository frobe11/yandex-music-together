from flask import redirect, Blueprint, request, jsonify
from yandex_music import Client
from app import app
from app.DB import AddUser, VerifyUser



@app.route('/')
def home():
    return "cum"
@app.route("/musics/<string:token>")
def musics(token):
    print(token)
    print(TOKEN)
    try:
    # Инициализация клиента с таймаутом
        client = Client(token=token).init()
        
        # Проверка авторизации
        if not client.me:
            print("Ошибка: Не удалось авторизоваться")
        else:
            print("Успешная авторизация!")
            print(f"Логин: {client.me.account.login}")
            print(f"Права: {client.me.account.first_name}")
        liked_tracks = client.users_likes_tracks()
        print(liked_tracks[0])

        return str(liked_tracks[0])
    except Exception as e:
        print(f"Ошибка при инициализации клиента: {e}")
        return 400

auth_bp = Blueprint(
    'auth',
    __name__,
    url_prefix="/auth"
)

@auth_bp.route('/registration', methods=["POST"])
def registration():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    yandex_token = data.get('yandex_token')
    try:
        client = Client(token=yandex_token).init()
    except:
        return jsonify({"message": "Invalid token"}), 400
    if not client.me:
        return jsonify({"message": "Invalid token"}), 400
    if not client.me.account:
        return jsonify({"message": "Invalid token"}), 400
    return AddUser(email, password, yandex_token, client=client)



@auth_bp.route('/login', methods=["POST"])
def login(): 
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    return VerifyUser(email=email, password=password)
