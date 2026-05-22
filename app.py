"""
Azure App Service Python Web Application
This is a sample Flask application ready for deployment on Azure App Service
"""
import os
from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# Configuration
app.config['DEBUG'] = os.getenv('FLASK_ENV', 'production') == 'development'
PORT = int(os.getenv('PORT', 8000))
ENVIRONMENT = os.getenv('ENVIRONMENT', 'Production')


@app.route('/')
def home():
    """Home page endpoint"""
    return render_template('index.html', environment=ENVIRONMENT)


@app.route('/api/health')
def health():
    """Health check endpoint for Azure App Service"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'environment': ENVIRONMENT,
        'version': '1.0.0'
    }), 200


@app.route('/api/info')
def info():
    """Application information endpoint"""
    return jsonify({
        'app_name': 'Refueling Platform',
        'version': '1.0.0',
        'environment': ENVIRONMENT,
        'python_version': os.sys.version,
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@app.route('/api/status')
def status():
    """Application status endpoint"""
    return jsonify({
        'running': True,
        'uptime': 'Active',
        'environment': ENVIRONMENT,
        'service': 'Azure App Service'
    }), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Not found', 'status': 404}), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error', 'status': 500}), 500


if __name__ == '__main__':
    # This is used when running locally
    app.run(host='0.0.0.0', port=PORT, debug=app.config['DEBUG'])
