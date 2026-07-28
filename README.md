# Customer Segmentation using K-Means Clustering with Interactive Dashboard

## Project Overview

This project performs customer segmentation using the **K-Means Clustering** algorithm on the **Olist Brazilian E-Commerce Dataset**. The goal is to group customers based on their purchasing behavior, enabling businesses to implement personalized marketing strategies, improve customer retention, and optimize business decisions.

The project also includes a **Flask REST API** and an **interactive dashboard** for visualizing customer segments and predicting the segment of new customers.

---

## Features

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Customer Segmentation using K-Means Clustering
- Elbow Method & Silhouette Score for optimal cluster selection
- PCA-based Cluster Visualization
- Flask REST API
- Interactive Dashboard
- Customer Segment Prediction
- Business Recommendations for each customer segment

---

## Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn

### Backend
- Flask
- Flask-CORS

### Frontend
- React
- Tailwind CSS

### Version Control
- Git
- GitHub

---

## Dataset

Dataset Used:

**Olist Brazilian E-Commerce Public Dataset**

The dataset contains information about:

- Customers
- Orders
- Payments
- Order Items
- Products

---

## Project Workflow

```
Raw Dataset
      │
      ▼
Data Understanding
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Data Merging
      │
      ▼
Feature Engineering
      │
      ▼
Data Preprocessing
      │
      ▼
K-Means Clustering
      │
      ▼
Customer Segments
      │
      ▼
Flask REST API
      │
      ▼
Interactive Dashboard
```

---

## Feature Engineering

The following customer behavior features were created:

- Recency
- Frequency
- Monetary Value
- Total Freight
- Average Product Price
- Total Products Purchased
- Average Installments
- Preferred Payment Method

---

## Machine Learning

Algorithm Used:

- K-Means Clustering

Model Evaluation:

- Elbow Method
- Silhouette Score
- PCA Visualization

---

## Project Structure

```
customer-segmentation-kmeans-dashboard/

│
├── backend/
│   ├── app.py
│   ├── prediction.py
│   ├── routes.py
│   ├── utils.py
│   └── models/
│       ├── scaler.pkl
│       └── kmeans.pkl
│
├── frontend/
│
├── datasets/
│   └── cleaned/
│       ├── customer_features.csv
│       ├── customer_features_scaled.csv
│       └── customer_segments.csv
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_data_analysis.ipynb
│   ├── 04_data_merging.ipynb
│   ├── 05_feature_engineering.ipynb
│   ├── 06_data_preprocessing.ipynb
│   └── 07_kmeans_clustering.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/customer-segmentation-kmeans-dashboard.git
```

Move into the project directory

```bash
cd customer-segmentation-kmeans-dashboard
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Backend

```bash
cd backend

python app.py
```

The backend will start at:

```
http://127.0.0.1:5000
```

---

## API Endpoints

### Dashboard Summary

```
GET /dashboard
```

Returns dashboard KPIs and cluster distribution.

---

### Cluster Statistics

```
GET /clusters
```

Returns statistics and business insights for each cluster.

---

### Predict Customer Segment

```
POST /predict
```

Example Request

```json
{
  "Recency": 20,
  "Frequency": 5,
  "Monetary": 1500,
  "Total_Freight": 180,
  "Average_Product_Price": 320,
  "Total_Products": 6,
  "Average_Installments": 3,
  "Preferred_Payment": "credit_card"
}
```

Example Response

```json
{
  "cluster": 2,
  "cluster_name": "Loyal Customers",
  "recommendation": "Reward loyal customers with personalized offers."
}
```

---

## Results

- Successfully segmented customers into meaningful groups.
- Built an interactive dashboard for visualization.
- Implemented real-time customer segment prediction.
- Generated actionable business recommendations.
- Improved customer understanding for targeted marketing strategies.

---

## Future Enhancements

- Real-time Database Integration
- Customer Lifetime Value Prediction
- Recommendation System
- Deep Learning-based Customer Segmentation
- Cloud Deployment
- User Authentication
- Docker Containerization

---

## Skills Demonstrated

- Data Cleaning
- Data Analysis
- Feature Engineering
- Machine Learning
- Unsupervised Learning
- Model Evaluation
- REST API Development
- Dashboard Development
- Data Visualization
- Git & GitHub

---

## Author

**Elango S**

B.Tech Artificial Intelligence and Data Science

Machine Learning | Data Science | Full Stack Development

---

## License

This project is licensed under the MIT License.
