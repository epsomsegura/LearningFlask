from flask import Flask
from .routes import IndexRoutes

app = Flask(__name__)


def init_app(config):
    # Configurations
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(IndexRoutes.main, url_prefix="/")

    return app
