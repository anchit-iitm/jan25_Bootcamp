# SQLALCHEMY_DATABASE_URI = 'sqlite:///data.sqlite3'
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.sqlite3'
    SECRET_KEY = "shhh..secret"
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'
    SECURITY_REDIRECT_BEHAVIOR = "spa"

    SECURITY_FLASH_MESSAGES = False

class localdev(Config):
    DEBUG = True


