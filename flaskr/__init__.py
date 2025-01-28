from flask import Flask
from flask_restful import Api
from flaskr.routes import load_routes
from flaskr.database import db
import os


def create_app():
    app = Flask(__name__)
    api = Api(app)

    env = os.environ.get('ENV', 'development')

    if env == 'development':
        app.config.from_pyfile('config.cfg')
    else:
        user = os.environ['USER']
        password = os.environ['PASSWORD']
        host = os.environ['HOST']
        port = os.environ['PORT']
        database = os.environ['DATABASE']
        database_url = (
            f'postgresql+psycopg://{user}:{password}@{host}:{port}/{database}'
        )
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_ECHO'] = True

    db.init_app(app)

    load_routes(api)

    return app
