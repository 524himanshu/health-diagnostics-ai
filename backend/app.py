from flask import Flask
from routes.symptoms import symptoms_bp
from routes.reports import reports_bp

app = Flask(__name__)

# Registering blueprints
app.register_blueprint(symptoms_bp, url_prefix='/api/symptoms')
app.register_blueprint(reports_bp, url_prefix='/api/report')

if __name__ == '__main__':
    app.run(debug=True)
