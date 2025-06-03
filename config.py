from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    PORT = os.getenv("PORT", 8000)
    DEBUG = False

class Dev(Config):
    DEBUG = True

class Prod(Config):
    DEBUG = False