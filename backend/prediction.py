import pandas as pd

from utils import (
    scaler,
    kmeans,
    CLUSTER_NAMES,
    BUSINESS_RECOMMENDATIONS
)

# -----------------------------------------------------
# Feature order (must match training data exactly)
# -----------------------------------------------------

FEATURE_COLUMNS = [

    "Recency",
    "Frequency",
    "Monetary",
    "Total_Freight",
    "Average_Product_Price",
    "Total_Products",
    "Average_Installments",

    "Preferred_Payment_credit_card",
    "Preferred_Payment_debit_card",
    "Preferred_Payment_voucher",
    "Preferred_Payment_boleto"

]

# -----------------------------------------------------
# Prediction Function
# -----------------------------------------------------

def predict_customer(data):

    payment = data["Preferred_Payment"]

    row = {

        "Recency": data["Recency"],
        "Frequency": data["Frequency"],
        "Monetary": data["Monetary"],
        "Total_Freight": data["Total_Freight"],
        "Average_Product_Price": data["Average_Product_Price"],
        "Total_Products": data["Total_Products"],
        "Average_Installments": data["Average_Installments"],

        "Preferred_Payment_credit_card": 0,
        "Preferred_Payment_debit_card": 0,
        "Preferred_Payment_voucher": 0,
        "Preferred_Payment_boleto": 0

    }

    if payment == "credit_card":
        row["Preferred_Payment_credit_card"] = 1

    elif payment == "debit_card":
        row["Preferred_Payment_debit_card"] = 1

    elif payment == "voucher":
        row["Preferred_Payment_voucher"] = 1

    elif payment == "boleto":
        row["Preferred_Payment_boleto"] = 1

    df = pd.DataFrame([row])

    df = df[FEATURE_COLUMNS]

    scaled = scaler.transform(df)

    cluster = int(kmeans.predict(scaled)[0])

    cluster_name = CLUSTER_NAMES[cluster]

    recommendation = BUSINESS_RECOMMENDATIONS[cluster_name]

    return {

        "cluster": cluster,

        "cluster_name": cluster_name,

        "recommendation": recommendation

    }