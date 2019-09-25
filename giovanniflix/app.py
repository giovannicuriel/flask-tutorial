"""
app.py
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_root():
    return "I am g-root"

if __name__ == '__main__':
    app.run(host='0.0.0.0')