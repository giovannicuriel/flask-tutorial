"""
app.py
"""
from flask import Flask, request, render_template
from uuid import uuid4
import json

app = Flask(__name__, template_folder="./templates")

content_storage = []


def print_request_info():
    print(">> Request data: ")
    print("Method: {}".format(request.method))
    print("Headers: {}".format(request.headers))
    print("Querystring: {}".format(request.query_string))
    print("Path: {}".format(request.path))
    print("Args: {}".format(request.args))

# methods=["GET", "HEAD", "POST", "PUT", "DELETE", "PATCH"]
# methods=["OPTIONS"]
# methods=["TRACE", "CONNECT"]
@app.route("/content", methods=["GET"])
def get_all_content():
    # Print request info
    print_request_info()
    return render_template("content.html", content_list=content_storage)

@app.route("/content", methods=["POST"])
def post_content():
    # Print request info
    print_request_info()
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

@app.route("/")
def get_root():
    return render_template("index.html", title="MainPage")

if __name__ == '__main__':
    app.run(host='0.0.0.0')