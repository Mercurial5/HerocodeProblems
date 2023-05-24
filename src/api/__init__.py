from flask import Flask

app = Flask(__name__)


def create_app() -> Flask:
    from api.routes import problems
    app.register_blueprint(problems, url_prefix='/problems')

    return app
