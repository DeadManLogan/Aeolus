from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)

    from src.routes import weather_blueprint
    app.register_blueprint(weather_blueprint)

    return app
