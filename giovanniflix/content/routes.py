from flask import Blueprint, render_template, request
from uuid import uuid4
from giovanniflix.content.models import ContentEntry
from giovanniflix import db

bp = Blueprint('content_bp', __name__, template_folder="templates")

content_storage = []

@bp.route("/content", methods=["GET"])
def get_all_content():
    content_list = ContentEntry.query.all()
    return render_template("content.html", content_list=content_list)

@bp.route("/content", methods=["POST"])
def post_content():
    body = request.json
    data = {
        "id": "{}".format(uuid4()),
        "title": body["title"],
        "link": body["link"]
    }
    content_entry = ContentEntry(**data)
    db.session.add(content_entry)
    db.session.commit()
    return "<h1>Result</h1><br/>Content was published. ID is {}".format(data['id'])
