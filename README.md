# Hướng dẫn chạy FinalCode_Group6_LendingClub.ipynb

## 1. Yêu cầu hệ thống

### a. Môi trường
- Python 3.8 trở lên
- Anaconda (khuyến nghị) hoặc môi trường ảo `venv`/`virtualenv`

### b. Thư viện cần thiết
Các thư viện cần thiết đã được liệt kê trong `requirements.txt`. Nếu chưa có, hãy tạo tệp này với nội dung:

```
pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit
joblib
notebook
```

## 2. Cài đặt môi trường

### a. Sử dụng Anaconda
```bash
conda create -n lendingclub_env python=3.8 -y
conda activate lendingclub_env
pip install -r requirements.txt
```

### b. Sử dụng môi trường ảo (venv)
```bash
python -m venv lendingclub_env
source lendingclub_env/bin/activate  # Trên MacOS/Linux
lendingclub_env\Scripts\activate    # Trên Windows
pip install -r requirements.txt
```

## 3. Chạy Jupyter Notebook
```bash
jupyter notebook
```
Sau đó, mở file `FinalCode_Group6_LendingClub.ipynb` và chạy từng ô code.

## 4. Chạy ứng dụng Streamlit
Nếu có phần giao diện Streamlit trong mã nguồn, chạy lệnh:
```bash
streamlit run app.py
```
Ứng dụng sẽ chạy tại `http://localhost:8501/` trên trình duyệt.

## 5. Lưu ý
- Đảm bảo có tệp `best_model.pkl` và `scaler.pkl` trong thư mục làm việc.
- Nếu gặp lỗi liên quan đến thư viện, thử chạy `pip install -r requirements.txt` lại.
- Nếu Streamlit hiển thị cảnh báo, hãy thử chạy lại bằng Terminal thay vì trong Jupyter Notebook.

---
✅ **Sau khi thực hiện đầy đủ các bước trên, bạn có thể sử dụng mô hình dự đoán khả năng trả nợ.**

