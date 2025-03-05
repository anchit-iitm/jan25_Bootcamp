# SQLALCHEMY_DATABASE_URI = 'sqlite:///data.sqlite3'
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.sqlite3'
    SECRET_KEY = "shhh..secret"
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'
    SECURITY_REDIRECT_BEHAVIOR = "spa"

    SECURITY_FLASH_MESSAGES = False

class localdev(Config):
    DEBUG = True


    CACHE_TYPE = "RedisCache"
    CACHE_DEFAULT_TIMEOUT = 60
    CACHE_KEY_PREFIX = "grocery_store_"
    CACHE_REDIS_HOST = "localhost"
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 2

    MAIL_SERVER = "localhost"
    MAIL_PORT = 1025
    MAIL_DEFAULT_SENDER = "dont_reply@abc.com"

class celery_config():
    broker_url = 'redis://localhost:6379/0'
    result_backend = 'redis://localhost:6379/1'
    timezone = 'Asia/Kolkata'