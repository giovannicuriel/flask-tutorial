from flask import Blueprint, render_template, request
from uuid import uuid4

bp = Blueprint('content_bp', __name__, template_folder="templates")

content_storage = []

@bp.route("/content", methods=["GET"])
def get_all_content():
    return render_template("content.html", content_list=content_storage)

@bp.route("/content", methods=["POST"])
def post_content():
    body = request.json
    content_id = uuid4()
    content_title = body['title']
    content_link = body['link']
    content = {
        "id": content_id,
        "title": content_title,
        "link": content_link
    }
    content_storage.append(content)
    return "<h1>Result</h1><br/>Content was published. ID is {}".format(content_id)
