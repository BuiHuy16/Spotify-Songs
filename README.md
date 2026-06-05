# Spotify Hit Analysis 2023 🎧

## Tổng quan dự án

Dự án nghiên cứu mối quan hệ giữa hai đặc tính âm nhạc phổ biến là **Danceability** (độ dễ nhảy) và **Energy** (mức độ sôi động) với mức độ thành công của bài hát trên Spotify, được đo bằng số lượt nghe (**Streams**).

Thông qua các phương pháp phân tích thống kê, kiểm định tương quan, hồi quy tuyến tính và mô hình phân lớp, nghiên cứu nhằm trả lời câu hỏi:

> **Danceability và Energy có thực sự giúp một bài hát đạt nhiều lượt stream hơn trên Spotify hay không?**

---

## Câu hỏi nghiên cứu

### Giả thuyết nghiên cứu

*   $H_0$: Độ nhảy và năng lượng không có tác động hoặc tác động nghịch chiều đến lượt stream.
*   $H_1$: Độ nhảy và năng lượng có tác động thuận chiều tích cực đến lượt stream.

### Mục tiêu

* Phân tích phân phối và đặc điểm của dữ liệu Spotify Songs 2023.
* Đánh giá mối quan hệ giữa Danceability, Energy và Streams.
* Xây dựng mô hình hồi quy tuyến tính (OLS) để kiểm định tác động của các biến.
* Kiểm tra khả năng dự báo của Danceability và Energy thông qua mô hình phân lớp.
* Đưa ra kết luận dựa trên bằng chứng thống kê.

---

## Bộ dữ liệu

### Nguồn dữ liệu

Dataset: **Spotify Songs 2023 (Kaggle)**

### Quy mô dữ liệu

| Thông tin               | Giá trị |
| ----------------------- | ------- |
| Số bản ghi ban đầu      | 953     |
| Số bản ghi sau làm sạch | 952     |
| Số biến sử dụng         | 25      |

### Các biến chính

| Biến           | Vai trò                  |
| -------------- | ------------------------ |
| streams        | Biến phụ thuộc           |
| log_streams    | Streams sau biến đổi log |
| danceability_% | Biến độc lập             |
| energy_%       | Biến độc lập             |
| artist(s)_name | Biến phân loại           |
| released_year  | Biến thời gian           |

---

## Phương pháp nghiên cứu

* Làm sạch và tiền xử lý dữ liệu.
* Phân tích khám phá dữ liệu (EDA).
* Kiểm định tương quan bằng Pearson và Spearman.
* Xây dựng mô hình hồi quy tuyến tính (OLS).
* Kiểm chứng kết quả bằng mô hình phân lớp (Classification).

---

## Kết quả chính

* Danceability có tương quan âm rất yếu với Streams.
* Energy không có ý nghĩa thống kê.
* Mô hình OLS có khả năng giải thích rất thấp (R² ≈ 0.005).
* Mô hình Classification đạt ROC-AUC ≈ 0.54, gần mức dự đoán ngẫu nhiên.

---

## Kết luận

Kết quả nghiên cứu không ủng hộ giả thuyết rằng Danceability và Energy làm tăng số lượt stream trên Spotify. Thành công của bài hát có thể phụ thuộc nhiều hơn vào các yếu tố như marketing, viral trends, playlist coverage và danh tiếng nghệ sĩ.


### Hàm ý thực tiễn

Kết quả cho thấy thành công của một bài hát có thể phụ thuộc nhiều hơn vào:

* Marketing
* Viral TikTok
* Playlist Editorial
* Danh tiếng nghệ sĩ
* Fanbase

Thay vì chỉ dựa vào các đặc tính âm nhạc.

---

## Công nghệ sử dụng

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy
* Statsmodels
* Scikit-learn
* Jupyter Notebook

---

## Cấu trúc thư mục

```text
./
├── README.md
├── requirements.txt
├── util.py
├── datasets/
│   ├── raw/
│   │   └── top-spotify-songs-2023.csv
│   └── processed/
│       └── cleaned_spotify_2023.csv
├── notebooks/
│   ├── data_cleaning.ipynb
│   ├── eda_visualization.ipynb
│   ├── hypothesis_testing.ipynb
│   └── main.ipynb
├── reports/
│   └── figures/
└── venv_ds/  # Môi trường ảo Python cục bộ (nếu đã tạo)
```

## Hướng dẫn cài đặt

### 1. Tạo và kích hoạt môi trường ảo (khuyến nghị)

```bash
python -m venv venv_ds
```

PowerShell:

```powershell
venv_ds\Scripts\Activate.ps1
```

Command Prompt:

```cmd
venv_ds\Scripts\activate
```

### 2. Cập nhật pip và cài đặt phụ thuộc

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Chạy Jupyter Notebook

```bash
jupyter notebook
```

Sau khi Notebook mở, chọn file:

```text
notebooks/main.ipynb
```

và chạy tuần tự các cell.

---

## Thành viên nhóm

| MSSV     | Họ và tên     |
| -------- | ------------- |
| 24021512 | Bùi Công Huy  |
| 24021656 | Đào Minh Tuấn |

---

## Tài liệu tham khảo

* Spotify Songs 2023 Dataset (Kaggle)
* Pandas Documentation
* NumPy Documentation
* SciPy Documentation
* Statsmodels Documentation
* Scikit-learn Documentation
