"""
app.py
"""
from flask import Flask, request
from uuid import uuid4
import json

app = Flask(__name__)

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
    return "<h1>Content listing</h1>"

@app.route("/content", methods=["POST"])
def post_content():
    # Print request info
    print_request_info()

    content_id = uuid4()
    print("ContentID is {}".format(content_id))
    # Do stuff
    return "<h1>Result</h1><br/>Content was published. ID is {}".format(content_id)

@app.route("/")
def get_root():
    return "I am g-root"

if __name__ == '__main__':
    app.run(host='0.0.0.0')