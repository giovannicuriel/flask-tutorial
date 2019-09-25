from flask import Flask
def create_app():
    app = Flask(__name__, template_folder="templates")
    with app.app_context():
        from giovanniflix.content import routes
        app.register_blueprint(routes.bp)
        return app