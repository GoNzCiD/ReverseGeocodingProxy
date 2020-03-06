from flask import Flask

from reversegeocodingproxy.cache import cache
from reversegeocodingproxy.config import configure_app
from reversegeocodingproxy.reverse.controllers import reverse
from reversegeocodingproxy.utils import get_instance_folder_path

app = Flask(__name__, instance_path=get_instance_folder_path(), instance_relative_config=True)

configure_app(app)
cache.init_app(app)

app.register_blueprint(reverse, url_prefix='/reverse')
