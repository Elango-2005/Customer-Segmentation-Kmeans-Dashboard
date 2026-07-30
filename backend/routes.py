from flask import Blueprint, request, jsonify

from backend.prediction import predict_customer
from backend.utils import (
    dashboard_summary,
    cluster_statistics
)

api = Blueprint("api", __name__)
api = Blueprint("api", __name__)

# -------------------------------------------------------
# Dashboard Summary
# -------------------------------------------------------

@api.route("/dashboard", methods=["GET"])
def dashboard():

    return jsonify(
        dashboard_summary()
    )


# -------------------------------------------------------
# Cluster Statistics
# -------------------------------------------------------

@api.route("/clusters", methods=["GET"])
def clusters():

    return jsonify(
        cluster_statistics()
    )


# -------------------------------------------------------
# Customer Prediction
# -------------------------------------------------------

@api.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        result = predict_customer(data)

        return jsonify(result)

    except Exception as e:

        return jsonify({

            "success": False,
            "message": str(e)

        }), 500