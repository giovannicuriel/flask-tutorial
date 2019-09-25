"""
app.py
"""
from flask import Flask, request, render_template
from uuid import uuid4
from giovanniflix.content import routes as content_routes
import json

app = Flask(__name__, template_folder="./templates")


@app.route("/")
def get_root():
    return render_template("index.html", title="MainPage")

app.register_blueprint(content_routes.bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0')