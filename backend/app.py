from flask import Flask, jsonify, send_from_directory
from routes.symptoms import symptoms_bp
from routes.reports import reports_bp
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_PATH = os.path.join(BASE_DIR, '../frontend')


app = Flask(__name__)

# Registering blueprints
app.register_blueprint(symptoms_bp, url_prefix='/api/symptoms')
app.register_blueprint(reports_bp, url_prefix='/api/report')

@app.route('/')
def home():
    return "Backend is running"

@app.route('/api/test')
def test():
    return {'message': 'API is working'}

@app.route('/routes', methods=['GET'])
def show_routes():
    return jsonify([str(rule) for rule in app.url_map.iter_rules()])


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
