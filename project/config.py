   
class Config(object):
    """Base config vars."""
    SECRET_KEY = '9OLWxND4o83j4Kty567pO'
class DevConfig(Config):
    DEBUG = True
    TESTING = True
    LOGIN_DISABLED = False 

