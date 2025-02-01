from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now()
    iso_date = now.isoformat(timespec='seconds')
    data = {
            "email": "ibotyle@gmail.com",
            "current_datetime": iso_date,
            "github_url": "https://github.com/ibotyle/code12"
            }
    return jsonify(data)
