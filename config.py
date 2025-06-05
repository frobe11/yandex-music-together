from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    PORT = os.getenv("PORT", 8000)
    HOST = os.getenv("HOST", "0.0.0.0")
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_COOKIE_SAMESITE = "Strict"

class Dev(Config):
    SQLALCHEMY_DATABASE_URI =os.getenv("DATABASELOCAL_URL")
    JWT_TOKEN_SECURE = False
    DEBUG = True

class Prod(Config):
    DEBUG = False
    HOST = os.getenv("HOST", "0.0.0.0")
    SQLALCHEMY_DATABASE_URI =os.getenv("DATABASEGLOBAL_URL")
    JWT_TOKEN_SECURE = True