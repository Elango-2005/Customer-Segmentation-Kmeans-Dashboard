import os

from flask import Flask
from flask_cors import CORS

from routes import api

app = Flask(__name__)

# Enable CORS for frontend
CORS(app)

# Register API routes
app.register_blueprint(api)

# Health Check
@app.route("/")
def home():
    return {
        "message": "Customer Segmentation API is Running 🚀",
        "status": "success"
    }

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )