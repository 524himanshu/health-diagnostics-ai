from flask import Flask
from routes.symptoms import symptoms_bp
from routes.reports import reports_bp
import os

app = Flask(__name__)

# Registering blueprints
app.register_blueprint(symptoms_bp, url_prefix='/api/symptoms')
app.register_blueprint(reports_bp, url_prefix='/api/report')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's port or default to 5000
    app.run(host='0.0.0.0', port=port)
