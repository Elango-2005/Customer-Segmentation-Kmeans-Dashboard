import pandas as pd

from backend.utils import (
    scaler,
    kmeans,
    CLUSTER_NAMES,
    BUSINESS_RECOMMENDATIONS
)

# -----------------------------------------------------
# Prediction Function
# -----------------------------------------------------

def predict_customer(data):

    row = {
        "Recency": data["Recency"],
        "Frequency": data["Frequency"],
        "Monetary": data["Monetary"],
        "Total_Freight": data["Total_Freight"],
        "Average_Product_Price": data["Average_Product_Price"],
        "Total_Products": data["Total_Products"],
        "Average_Installments": data["Average_Installments"],
        "Preferred_Payment": data["Preferred_Payment"]
    }

    # Create DataFrame
    df = pd.DataFrame([row])

    # One-hot encode exactly like training
    df = pd.get_dummies(
        df,
        columns=["Preferred_Payment"],
        drop_first=True
    )

    # Match training columns exactly
    df = df.reindex(
        columns=scaler.feature_names_in_,
        fill_value=0
    )

    # Scale
    scaled = scaler.transform(df)

    # Predict
    cluster = int(kmeans.predict(scaled)[0])

    cluster_name = CLUSTER_NAMES[cluster]

    recommendation = BUSINESS_RECOMMENDATIONS[cluster_name]

    return {
        "cluster": cluster,
        "cluster_name": cluster_name,
        "recommendation": recommendation
    }