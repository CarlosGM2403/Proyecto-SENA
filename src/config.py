class Config:
    SECRET_KEY = 'clave_super_secreta'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'proyecto'


config = {
    'development' : DevelopmentConfig
}