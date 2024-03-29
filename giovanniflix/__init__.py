from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder="templates")
    db.init_app(app)
    app.config.from_mapping({
        "SQLALCHEMY_DATABASE_URI": "sqlite:////tmp/db.sqlite",
        "FLASK_ADMIN_SWATCH": "cerulean",
        "SESSION_TYPE": "filesystem"
    })
    app.secret_key = "{}".format(uuid4())
    with app.app_context():
        from giovanniflix.content import routes
        app.register_blueprint(routes.bp)
        db.create_all()
        return app