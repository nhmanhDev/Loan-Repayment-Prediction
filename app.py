import streamlit as st
import pandas as pd
import numpy as np
import joblib
import base64

# Cấu hình trang
st.set_page_config(page_title="Dự đoán khả năng trả nợ", page_icon="💰")

def get_base64_image(image_path):
    """Đọc ảnh và chuyển thành Base64."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Đường dẫn ảnh nền
image_path = "lending_image.jpg"
base64_image = get_base64_image(image_path)

# CSS đặt ảnh nền
background_html = f"""
    <style>
        .stApp {{
            background-image: url("data:image/webp;base64,{base64_image}");
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
        }}
        
    </style>
"""

# Áp dụng CSS
st.markdown(background_html, unsafe_allow_html=True)

# CSS tùy chỉnh
st.markdown(
    """
    <style>
        .header { color: #8F87F1; text-align: center; font-size: 50px !important; font-weight: bold; }
        .custom-subheader { margin: 10px; background-color: #122f6b; color: #FFFFFF; padding: 12px; border-radius: 10px; text-align: center; font-size: 24px; font-weight: bold; }
        div.stButton > button { background-color: #125FB7 !important; color: white !important; border-radius: 8px !important; font-size: 18px !important; font-weight: bold; padding: 10px 20px !important; transition: 0.3s; }
        div.stButton > button:hover { background-color: #018EC1 !important; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
        .custom-label {
            margin: 0px;
            color: #004aad;
            font-weight: bold;
            font-size: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""<div class='custom-subheader'>Nhập thông tin</div>""", unsafe_allow_html=True)

# Tải mô hình và bộ scaler
model = joblib.load("rf_model.pkl")
scaler = joblib.load("scaler.pkl")

# Tạo form nhập liệu
with st.form(key="loan_form"):

    st.markdown('<p class="custom-label">Thu nhập(USD)</p>', unsafe_allow_html=True)
    annual_inc = st.number_input("1", min_value=0.0, max_value=1000000.0, value=100000.0)

    st.markdown('<p class="custom-label">Số tiền vay (USD)</p>', unsafe_allow_html=True)
    loan_amnt = st.number_input("1", min_value=0.0, max_value=1000000.0, value=50000.0)

    
    st.markdown('<p class="custom-label">Lãi suất (%)</p>', unsafe_allow_html=True)
    int_rate = st.number_input("2", min_value=0.0, max_value=100.0, value=10.0)

    st.markdown('<p class="custom-label">Số tài khoản tín dụng đang mở</p>', unsafe_allow_html=True)
    open_acc = st.number_input("3", min_value=0, max_value=100, value=1)

    st.markdown('<p class="custom-label">Tỷ lệ nợ trên thu nhập (DTI)</p>', unsafe_allow_html=True)
    dti = st.number_input("4", min_value=0.0, max_value=100.0, value=1.0)

    st.markdown('<p class="custom-label">Số lượng hồ sơ công khai</p>', unsafe_allow_html=True)
    pub_rec = st.number_input("5", min_value=0, max_value=100, value=1)

    st.markdown('<p class="custom-label">Năm mở tài khoản tín dụng đầu tiên</p>', unsafe_allow_html=True)
    earliest_cr_line = st.number_input("6", min_value=1900, max_value=2025, value=2005)

    st.markdown('<p class="custom-label">Tỷ lệ sử dụng tín dụng quay vòng (%)</p>', unsafe_allow_html=True)
    revol_util = st.number_input("7", min_value=0.0, max_value=100.0, value=5.0)

    st.markdown('<p class="custom-label">Số tài khoản thế chấp</p>', unsafe_allow_html=True)
    mort_acc = st.number_input("8", min_value=0, max_value=50, value=1)

    st.markdown('<p class="custom-label">Thời hạn vay</p>', unsafe_allow_html=True)
    term = st.selectbox("9", ["36 months", "60 months"])

    st.markdown('<p class="custom-label">Cấp tín dụng phụ</p>', unsafe_allow_html=True)
    sub_grade = st.selectbox("10", [f"{x}{y}" for x in "ABCDEFG" for y in range(1,6)])

    st.markdown('<p class="custom-label">Zip code</p>', unsafe_allow_html=True)
    zip_code = st.selectbox("11", ["70466", "22690", "30723", "48052", "00831", "29597", "05113", "11650", "93700", "86630"])

    st.markdown('<p class="custom-label">Loại hình sở hữu nhà</p>', unsafe_allow_html=True)
    home_ownership = st.selectbox("12", ["RENT", "MORTGAGE", "OTHER", "OWN"])

    st.markdown('<p class="custom-label">Mục đích vay</p>', unsafe_allow_html=True)
    purpose = st.selectbox("13", ["vacation", "debt_consolidation", "credit_card", "home_improvement", "small_business", "medical", "other", "wedding", "car", "moving", "house", "major_purchase", "educational", "renewable_energy"])

    st.markdown('<p class="custom-label">Loại đơn vay</p>', unsafe_allow_html=True)
    application_type = st.selectbox("14", ["Individual", "Joint", "DIRECT_PAY"])

    

    # Thêm nút submit
    submit_button = st.form_submit_button(label="Dự đoán")


if submit_button:
    input_data = pd.DataFrame({
        'loan_amnt': [loan_amnt],
        'int_rate': [int_rate],
        
        'earliest_cr_line': [earliest_cr_line],
        'dti': [dti],
        'open_acc': [open_acc],
        'pub_rec': [pub_rec],
        'revol_util': [revol_util],
        
        'annual_inc': [annual_inc],

        'mort_acc': [mort_acc],
        
        'zip_code': [zip_code],
        'term': [term],
        'sub_grade': [sub_grade],
        
        'purpose': [purpose],
        'application_type': [application_type],
        
        'home_ownership': [home_ownership],
    })

    # data = pd.get_dummies(data, columns=['zip_code'], drop_first=True)

    input_data['zip_code'] = input_data['zip_code'].astype(int)

    zip_risk = {
        813: 0.00, 5113: 0.00, 29597: 0.00,
        93700: 1.00, 86630: 1.00, 11650: 1.00,
        70466: 0.80, 30723: 0.80, 22690: 0.80, 48052: 0.2
    }

    input_data['annual_inc'] = np.log1p(input_data['annual_inc'])

    input_data['zip_code'] = input_data['zip_code'].map(zip_risk)


    dummies = ['term', 'sub_grade', 'purpose', 'application_type', 'home_ownership']
    # input_data = pd.get_dummies(input_data, columns=dummies, drop_first=True)
    input_data = pd.get_dummies(input_data, columns=dummies)

    missing_cols = set(scaler.feature_names_in_) - set(input_data.columns)
    for col in missing_cols:
        input_data[col] = 0

    input_data = input_data[scaler.feature_names_in_]
    input_data_scaled = scaler.transform(input_data)

    prediction = model.predict(input_data_scaled)[0]
    probability_fully_paid = model.predict_proba(input_data_scaled)[0][0]

    # Kiểm tra kết quả dự đoán và áp dụng màu sắc
    threshold = 0.5  # Ngưỡng xác suất để phân loại là "Fully Paid"
    if probability_fully_paid >= threshold:
        result_text = "✅ Fully Paid (Hoàn trả đầy đủ)"
        box_color = "#2FF93C"  # Xanh lá cây
    else:
        result_text = "❌ Charged Off (Vỡ nợ)"
        box_color = "#E2030A"  # Đỏ

    # Hiển thị kết quả với hộp màu
    st.markdown(
        f"""
        <div style="padding: 15px; border-radius: 10px; background-color: {box_color}; color: white; text-align: center; font-size: 18px; font-weight: bold;">
            {result_text}
        </div>
        <p style="text-align: center; font-size: 16px;"><b>Xác suất hoàn trả đầy đủ:</b> {probability_fully_paid:.2%}</p>
        """,
        unsafe_allow_html=True
    )


