from flask import Flask, jsonify
from time import sleep
import os

app = Flask(__name__)

delay_ms = os.environ.get('delay_ms', default=500)
delay_sec = int(delay_ms) / 1000


@app.route('/api/data')
def get_data():
    data = {"company": "UIDAI", "department": "DevOps"}
    sleep(delay_sec)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
