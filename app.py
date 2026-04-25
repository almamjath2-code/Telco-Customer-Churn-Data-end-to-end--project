#this is insght lock my model
import streamlit as st
import pandas as pd
import joblib

# 1️⃣ Load model & training columns
model = joblib.load("customer_churn_model.pkl")
train_columns = joblib.load("x_train_columns.pkl")

st.title("📊 Customer Churn Prediction App")

# 2️⃣ User Inputs
age = st.number_input("Age", min_value=0, max_value=100,value=0)#velue is ender data like new_customer_data of churn prediction
tenure = st.number_input("Tenure (months)", min_value=0, value=0)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=0.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=0.0)

gender = st.selectbox("Gender", ["select", "female", "male"])
contract = st.selectbox("Contract", ["select","Month-to-month", "One year", "Two year"])
payment_method = st.selectbox("Payment Method", ["select", "Electronic check", "Mailed check", "Bank transfer", "Credit card"])


# 3️⃣ Prediction button
if st.button("Predict"):
    
    # 4️⃣ Create input DataFrame
    input_df = pd.DataFrame([{
        "Age": age,
        "Tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }])
    
    # 5️⃣ Create all category columns = 0
    for col in train_columns:
        if col.startswith("Gender_") or col.startswith("Contract_") or col.startswith("PaymentMethod_"):
            input_df[col] = 0
    
    # 6️⃣ Set the correct category values = 1
    input_df["Gender_" + gender] = 1
    input_df["Contract_" + contract] = 1
    input_df["PaymentMethod_" + payment_method] = 1
    
    # 7️⃣ Match training columns
    input_df = input_df.reindex(columns=train_columns, fill_value=0)
    
    # 8️⃣ Make prediction
    prediction = model.predict(input_df)[0]
    
    # Optional probability (only for classification models)
    if hasattr(model, "predict_proba"):
        prob = model.predict_proba(input_df)[0][1]
        st.write(f"🔥 Churn Probability: {prob:.2f}")
    
    # Show prediction
    if prediction == 1:
        st.error("❌ Customer will Churn")
    else:
        st.success("✅ Customer will Stay")


        # Save new input data to CSV (optional)
# if st.button("Save Input"):
#     new_data = pd.DataFrame({"km":[km], "year":[year], "price":[price]})
#     new_data.to_csv("user_inputs.csv", mode='a', index=False, header=False)
#     st.success("Data saved!")


# this afret use api 

# import streamlit as st
# import requests

# st.title("📊 Customer Churn App (API Version)")

# age = st.number_input("Age")
# tenure = st.number_input("Tenure")
# monthly = st.number_input("Monthly Charges")
# total = st.number_input("Total Charges")

# gender = st.selectbox("Gender", ["female", "male"])
# contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
# payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])

# if st.button("Predict"):

#     response = requests.post(
#         "http://127.0.0.1:8000/predict_churn",
#         json={
#             "age": age,
#             "tenure": tenure,
#             "monthly_charges": monthly,
#             "total_charges": total,
#             "gender": gender,
#             "contract": contract,
#             "payment_method": payment
#         }
#     )

#     result = response.json()

#     if result["prediction"] == 1:
#         st.error("❌ Customer will Churn")
#     else:
#         st.success("✅ Customer will Stay")

#     st.write("🔥 Probability:", result["churn_probability"])