from flask import Flask, jsonify
from time import sleep
import os
import requests

app = Flask(__name__)
delay_ms = os.environ.get('DELAY_MS', default=500)
print(delay_ms)
delay_sec = int(delay_ms) / 1000

tail_api_url = os.environ.get('TAIL_URL', default='http://tail:8001/api/data')
print(tail_api_url)


@app.route('/api/data')
def get_data():
    sleep(delay_sec)
    response = requests.get(tail_api_url)

    if response.status_code == 200:
        data = response.json()
    else:
        data = {"status": "Error", "error_code": response.status_code}

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
