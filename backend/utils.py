import os
import joblib
import pandas as pd

# backend/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Project root (Customer-Segmentation/)
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# Models
MODELS_DIR = os.path.join(BASE_DIR, "models")

# Dataset
DATASET_DIR = os.path.join(PROJECT_ROOT, "datasets", "cleaned")

# ----------------------------------------------------
# Load Machine Learning Models
# ----------------------------------------------------

scaler = joblib.load(
    os.path.join(MODELS_DIR, "scaler.pkl")
)

kmeans = joblib.load(
    os.path.join(MODELS_DIR, "kmeans.pkl")
)

# ----------------------------------------------------
# Load Customer Dataset
# ----------------------------------------------------
customer_data = pd.read_csv(
    os.path.join(
        DATASET_DIR,
        "customer_segments.csv"
    )
)

# ----------------------------------------------------
# Cluster Names
# ----------------------------------------------------

CLUSTER_NAMES = {
    0: "High Value Customers",
    1: "Loyal Customers",
    2: "Regular Customers",
    3: "Occasional Buyers",
    4: "At-Risk Customers",
    5: "New Customers"
}

# ----------------------------------------------------
# Business Recommendations
# ----------------------------------------------------

BUSINESS_RECOMMENDATIONS = {

    "High Value Customers":
        "Offer premium membership, VIP rewards and exclusive discounts.",

    "Loyal Customers":
        "Reward loyalty with cashback, reward points and personalized offers.",

    "Regular Customers":
        "Recommend products based on previous purchases to increase spending.",

    "Occasional Buyers":
        "Send seasonal promotions and reminder notifications.",

    "At-Risk Customers":
        "Launch win-back campaigns with special discounts.",

    "New Customers":
        "Welcome them with onboarding offers and first-purchase coupons."
}

# ----------------------------------------------------
# Dashboard Summary
# ----------------------------------------------------

def dashboard_summary():

    return {

        "total_customers": int(len(customer_data)),

        "clusters": int(customer_data["Cluster"].nunique()),

        "average_monetary":
            round(customer_data["Monetary"].mean(),2),

        "average_frequency":
            round(customer_data["Frequency"].mean(),2),

        "cluster_distribution":
            customer_data["Cluster"]
            .value_counts()
            .sort_index()
            .to_dict()
    }


# ----------------------------------------------------
# Cluster Statistics
# ----------------------------------------------------

def cluster_statistics():

    summary = (

        customer_data

        .groupby("Cluster")[

            [

                "Recency",

                "Frequency",

                "Monetary",

                "Total_Freight",

                "Average_Product_Price",

                "Total_Products",

                "Average_Installments"

            ]

        ]

        .mean()

        .round(2)

        .reset_index()

    )

    summary["Cluster_Name"] = summary["Cluster"].map(CLUSTER_NAMES)

    summary["Recommendation"] = summary["Cluster_Name"].map(

        BUSINESS_RECOMMENDATIONS

    )

    return summary.to_dict(orient="records")