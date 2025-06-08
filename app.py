from flask import Flask, request, jsonify, render_template_string
from datetime import datetime

app = Flask(__name__)
data_log = []

@app.route('/')
def home():
    return "<h2>🚢 RAK Webhook Receiver is Running</h2><p>POST data to /post-data</p>"

@app.route('/post-data', methods=['POST'])
def receive_data():
    payload = request.json
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "data": payload
    }
    data_log.append(entry)
    print("Received:", entry)
    return jsonify({"status": "OK"}), 200

@app.route('/view')
def view_data():
    html = """
    <h2>📋 Latest Sensor Data</h2>
    <ul>
    {% for item in data %}
      <li><strong>{{ item.timestamp }}</strong>: {{ item.data }}</li>
    {% endfor %}
    </ul>
    """
    return render_template_string(html, data=data_log[-10:])
