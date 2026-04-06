# Customer Churn Prediction Project
# 📌  Project Overview

This project aims to predict customer churn for a telecommunications company. Churn occurs when a customer stops using the company’s service. Predicting churn helps businesses identify at-risk customers and implement strategies to retain them.

The project uses historical customer data, applies data preprocessing, exploratory data analysis (EDA), and machine learning models to predict whether a customer will churn or not.

# 🗂 Dataset

The dataset contains information about customers such as demographics, account information, and usage metrics.

# Key Features:
Age – Age of the customer (in years)
Gender – Customer’s gender
Tenure – Number of months the customer has stayed
MonthlyCharges – Monthly billing amount
TotalCharges – Total billing amount
Contract – Type of contract (Month-to-Month, One Year, Two Year)
PaymentMethod – How the customer pays
Churn – Target variable (Yes = churned, No = retained)

# Data Source: [Mention your dataset source, e.g., Kaggle or internal dataset]

# 🛠 Tools & Technologies
Python – Main programming language
Pandas & NumPy – Data manipulation
Matplotlib & Seaborn – Data visualization
Scipy – Detecting and handling outliers (e.g., using z-score or IQR methods)
Scikit-learn – Machine learning algorithms & evaluation
Streamlit – Web app for interactive predictions
Joblib / Pickle – Model serialization
# 🧹 Data Preprocessing
Handling missing values
Encoding categorical variables (Label Encoding / One-Hot Encoding)
Feature scaling
Train-test split for model validation

# 📊 Exploratory Data Analysis (EDA)
Visualizations to understand distributions and patterns
Correlation analysis between features
Identifying trends related to churn
# 🤖 Machine Learning Models

# The following models were trained and evaluated:

Model	            Accuracy	Precision	Recall	F1-Score
Random Forest test	  0.76	        0.68	   0.56	   0.61
Random Forest train    0.75         0.67        0.55    0.60

Best Model: Random Forest (example, update with your results)

# Feature Importance: Shows which features most influence churn prediction.

# 🚀 Streamlit Web App

An interactive app allows users to input customer information and predict churn in real-time.



# How to run the app:

```bash
pip install -r requirements.txt
streamlit run app.py


# 📈 Project Workflow
Load dataset
Data cleaning & preprocessing
Exploratory data analysis
Feature engineering & encoding
Model training & evaluation
Save the best model (.pkl file)
Build Streamlit app for real-time predictions


# 💡 Insights
Customers with month-to-month contracts have higher churn rates
High monthly charges correlate with higher churn
Longer tenure reduces the likelihood of churn

# ⚡ Future Improvements
Hyperparameter tuning to improve model accuracy
Incorporate additional features (e.g., customer complaints, usage patterns)
Deploy on cloud platforms for wider access
📁 Project Structure
customer_churn_project/
│
├─ data/               # Dataset files
├─ notebooks/          # EDA & model experimentation
├─ app.py              # Streamlit web app
├─ model.pkl           # Saved trained model
├─ requirements.txt    # Python dependencies
└─ README.md           # Project description

# For questions or suggestions:
Name: Amjath
Email: almamjath2@gmail.com