from flask import Flask
from flask_restful import Api
from flaskr.routes import load_routes
from flaskr.database import db


def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config.from_pyfile('config.cfg')
    db.init_app(app)

    load_routes(api)

    return app
