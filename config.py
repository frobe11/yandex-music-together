from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    PORT = os.getenv("PORT", 8000)
    HOST = os.getenv("HOST", "0.0.0.0")
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Dev(Config):
    SQLALCHEMY_DATABASE_URI =os.getenv("DATABASELOCAL_URL")
    DEBUG = True

class Prod(Config):
    DEBUG = False
    HOST = os.getenv("HOST", "0.0.0.0")
    SQLALCHEMY_DATABASE_URI =os.getenv("DATABASEGLOBAL_URL")