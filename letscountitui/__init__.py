import os

from dotenv import load_dotenv
from flask import Flask
from loguru import logger

from letscountitui.routes.counter_routes import bp as counter_bp
from letscountitui.routes.home_routes import bp as home_bp

load_dotenv()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    #     SERVER_NAME='localhost:5000'
    # )

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)
    logger.debug(f'FLASK_ENV: {os.environ.get("FLASK_ENV")}')
    if os.environ.get("FLASK_ENV") == "development":
        app.config.from_object("letscountitui.config.config.DevelopmentConfig")
    else:
        app.config.from_object("letscountitui.config.config.ProductionConfig")
    # app.config.from_object('letscountitui.config.Config')

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    @app.route("/health")
    def health():
        return "Healthy"

    app.register_blueprint(home_bp)
    app.register_blueprint(counter_bp)

    return app
