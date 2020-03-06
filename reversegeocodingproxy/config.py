import os

from flask_compress import Compress


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    CACHE_TYPE = "simple"
    COMPRESS_MIMETYPES = [
        "text/html",
        "text/css",
        "text/xml",
        "application/json",
        "application/javascript",
    ]
    COMPRESS_LEVEL = 6
    COMPRESS_MIN_SIZE = 500


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    ENV = "development"
    # LOCAL_SERVER = "local"
    # REMOTE_SERVER = "remote"


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    ENV = "production"


config = {
    "dev": "reversegeocodingproxy.config.DevelopmentConfig",
    "prod": "reversegeocodingproxy.config.ProductionConfig",
    "default": "reversegeocodingproxy.config.DevelopmentConfig",
}


def configure_app(app):
    config_name = os.getenv("FLASK_CONFIGURATION", "default")
    app.config.from_object(config[config_name])
    app.config.from_pyfile("config.cfg")
    # Configure Compressing
    Compress(app)
