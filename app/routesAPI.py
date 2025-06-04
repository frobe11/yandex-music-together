from flask import redirect, Blueprint, request, jsonify
from yandex_music import ClientAsync
import requests
from app import app
from app.DB import AddUser



@app.route('/')
def home():
    return "cum"
@app.route("/musics/<string:token>")
async def musics(token):
    print(token)
    print(TOKEN)
    try:
    # Инициализация клиента с таймаутом
        client = await ClientAsync(token=token).init()
        
        # Проверка авторизации
        if not client.me:
            print("Ошибка: Не удалось авторизоваться")
        else:
            print("Успешная авторизация!")
            print(f"Логин: {client.me.account.login}")
            print(f"Права: {client.me.account.first_name}")
        liked_tracks = await client.users_likes_tracks()
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
    return AddUser(email, password, yandex_token)



@auth_bp.route('/login')
def login(): 
    code = request.args.get("code")
    if not code:
        return "Empty code", 400
    token_url = "https://oauth.yandex.ru/token"
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    responce = requests.post(token_url, data=data)
    token_data = responce.json()
    print(token_data)
    token = token_data.get("access_token")
    if not token:
        return "Empty token", 400
    else:
        TOKEN = token
        return f"ТОКЕН: {token}"