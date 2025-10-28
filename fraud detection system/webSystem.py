import streamlit as st
import pandas as pd
import joblib

model = joblib.load('fraud detection system.pkl')

st.title("Fraud Detection System App")

st.markdown("Please enter the transaction detailes and use the predict button")

st.divider()

transaction_type = st.selectbox("Transaction Type",['PAYMENT', 'TRANSFER', 'CASH_OUT','DEPOSIT'])
amount = st.number_input('amount', min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input('old balance (sender)', min_value=0.0, value=10000.0)
newbalanaceOrig = st.number_input('new balance (sender)', min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input('old balance (receiver)', min_value=0.0, value=0.0)
newbalanaceDest = st.number_input('new balance (receiver)', min_value=0.0, value=0.0)

if st.button('Predict'):
    input_data = pd.DataFrame([{
        'type' : transaction_type,
        'amount' : amount,
        'oldbalanceOrg' : oldbalanceOrg,
        'newbalanceOrig' : newbalanaceOrig,
        'oldbalanceDest' : oldbalanceDest,
        'newbalanceDest' : newbalanaceDest 
    }])

    input_data['balancedDest'] = input_data['newbalanceDest'] - input_data['oldbalanceDest']

    prediction = model.predict(input_data)[0]

    st.subheader(f'Prediction : {int(prediction)}')

    if prediction == 1:
        st.error("This prediction can be fraud")
    else :
        st.success("This prediction looks like it is not a fraud")
