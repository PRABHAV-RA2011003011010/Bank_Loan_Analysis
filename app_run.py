import joblib
import streamlit as st
import pandas as pd

def check_status(ia,la,lt,cs,ta):
    
    input_data = pd.DataFrame({
        'income_annum': [ia],
        'loan_amount': [la],
        'loan_term': [lt],
        'cibil_score': [cs],
        'total_assets': [ta]
    })
    standardized_data = scaler_loaded.transform(input_data)
    prediction = rf_final_loaded.predict(standardized_data)
    
    return 'Approved' if prediction[0] == 0 else 'Rejected'


rf_final_loaded = joblib.load('rf_final_model.joblib')
scaler_loaded = joblib.load('scaler.joblib')
st.title('Loan Approval Pridictor')

income_annum=st.number_input('What is your annual income?')
loan_amount=st.number_input('Amount of loan required?')
loan_term=st.number_input('Duration(in months) required to repay?')
cibil_score=st.number_input('Your cibil score?')
total_assets=st.number_input('Your assests valuation?')

if st.button('Predict'):
    recommendations= check_status(int(income_annum),int(loan_amount),int(loan_term),int(cibil_score),int(total_assets))
    
    st.write(recommendations)