import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Cấu hình trang
st.set_page_config(page_title="Dự đoán khả năng trả nợ", page_icon="💰")

# CSS tùy chỉnh
st.markdown(
    """
    <style>
        .stApp { background-color: #87CEEB !important; }
        .header { color: #8F87F1; text-align: center; font-size: 50px !important; font-weight: bold; }
        .custom-subheader { margin: 10px; background-color: #FFDCCC; color: #FF8989; padding: 12px; border-radius: 10px; text-align: center; font-size: 24px; font-weight: bold; }
        div.stButton > button { background-color: #4CAF50 !important; color: white !important; border-radius: 8px !important; font-size: 18px !important; font-weight: bold; padding: 10px 20px !important; transition: 0.3s; }
        div.stButton > button:hover { background-color: #45a049 !important; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""<div class='custom-subheader'>Nhập thông tin</div>""", unsafe_allow_html=True)

# Tải mô hình và bộ scaler
model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

with st.form(key='loan_form'):
    loan_amnt = st.number_input("Số tiền vay (USD)", min_value=0.0, max_value=100000.0, value=1000.0)
    int_rate = st.number_input("Lãi suất (%)", min_value=0.0, max_value=100.0, value=1.0)
    open_acc = st.number_input("Số tài khoản tín dụng đang mở", min_value=0, max_value=100, value=1)
    dti = st.number_input("Tỷ lệ nợ trên thu nhập (DTI)", min_value=0.0, max_value=100.0, value=1.0)
    pub_rec = st.number_input("Số lượng hồ sơ công khai", min_value=0, max_value=100, value=1)
    earliest_cr_line = st.number_input("Năm mở tài khoản tín dụng đầu tiên", min_value=1900, max_value=2025, value=2005)
    revol_util = st.number_input("Tỷ lệ sử dụng tín dụng quay vòng (%)", min_value=0.0, max_value=100.0, value=5.0)
    mort_acc = st.number_input("Số tài khoản thế chấp", min_value=0, max_value=50, value=1)

    term = st.selectbox("Thời hạn vay", ["36 months", "60 months"])
    sub_grade = st.selectbox("Cấp tín dụng phụ", [f"{x}{y}" for x in "ABCDEFG" for y in range(1,6)])
    zip_code = st.selectbox("Zip code", ["70466", "22690", "30723", "48052", "00831", "29597", "05113", "11650", "93700", "86630"])
    home_ownership = st.selectbox("Loại hình sở hữu nhà", ["RENT", "MORTGAGE", "OTHER", "OWN"])
    purpose = st.selectbox("Mục đích vay", ["vacation", "debt_consolidation", "credit_card", "home_improvement", "small_business", "medical", "other", "wedding", "car", "moving", "house", "major_purchase", "educational", "renewable_energy"])
    application_type = st.selectbox("Loại đơn vay", ["Individual", "Joint", "DIRECT_PAY"])

    submit_button = st.form_submit_button(label="Dự đoán")

if submit_button:
    input_data = pd.DataFrame({
        'loan_amnt': [loan_amnt],
        'int_rate': [int_rate],
        'open_acc': [open_acc],
        'dti': [dti],
        'pub_rec': [pub_rec],
        'revol_util': [revol_util],
        'earliest_cr_line': [earliest_cr_line],
        'mort_acc': [mort_acc],
        'term': [term],
        'sub_grade': [sub_grade],
        'zip_code': [zip_code],
        'home_ownership': [home_ownership],
        'purpose': [purpose],
        'application_type': [application_type],
    })

    dummies = ['term', 'sub_grade', 'zip_code', 'home_ownership', 'purpose', 'application_type']
    input_data = pd.get_dummies(input_data, columns=dummies)

    missing_cols = set(scaler.feature_names_in_) - set(input_data.columns)
    for col in missing_cols:
        input_data[col] = 0

    input_data = input_data[scaler.feature_names_in_]
    input_data_scaled = scaler.transform(input_data)

    prediction = model.predict(input_data_scaled)[0]
    probability_fully_paid = model.predict_proba(input_data_scaled)[0][0]

    result = "✅ **Fully Paid (Hoàn trả đầy đủ)**" if prediction == 0 else "❌ **Charged Off (Vỡ nợ)**"
    st.write(f"Kết quả dự đoán: {result}")
    st.write(f"Xác suất hoàn trả đầy đủ: {probability_fully_paid:.2%}")
