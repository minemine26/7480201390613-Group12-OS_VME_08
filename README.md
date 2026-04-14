# 🖥️ Đồ án Hệ Điều Hành – Mô phỏng thuật toán thay thế trang

**Project Name:** Demo Virtual Memory Management Algorithm: LRU, FIFO, OPT
**Project Code:** OS_VME_08

---

## 👥 Thành viên

| STT | Họ và tên             | MSSV         |
| --- | --------------------- | ------------ |
| 1   | Trần Ngọc Mai         | 089305019922 |
| 2   | Nguyễn Đoàn Thành Đạt | 033206000242 |
| 3   | Nguyễn Văn Minh Đức   | 066206007328 |

---

## 📌 Giới thiệu

Đồ án xây dựng hệ thống mô phỏng các thuật toán thay thế trang trong quản lý bộ nhớ ảo, bao gồm:

* FIFO
* LRU
* OPT

Hệ thống hỗ trợ:

* Đọc dữ liệu từ file CSV
* Mô phỏng từng bước
* Hiển thị trạng thái khung trang
* Xuất kết quả ra CSV
* Hiển thị biểu đồ
* Giao diện GUI

---

## 🛠️ Công nghệ

* Python 3.8+
* PyQt5
* pandas, csv
* matplotlib
* Git, GitHub

---

## 📁 Cấu trúc project

```id="2xkqwx"
OS_PROJECT/
│
├── CODE/                    # Source code chính
│   ├── algorithms/          # Thuật toán (FIFO, LRU, OPT)
│   ├── engine/              # Simulation engine
│   ├── gui/                 # Giao diện PyQt5
│   ├── models/              # Data model
│   ├── utils/               # Xử lý file
│   └── main.py              # Logic chính của hệ thống
│
├── DOCX/                    # Báo cáo Word
├── input/                   # File CSV đầu vào
├── output/                  # File CSV kết quả
├── PPTX/                    # Slide thuyết trình
├── test/                    # Kiểm thử
│
├── main.py                  # Entry point (chạy từ root)
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🔍 Giải thích main.py

Dự án sử dụng 2 file `main.py`:

* `main.py` (root):
  → File chạy chính, dùng để start toàn bộ chương trình

* `CODE/main.py`:
  → Chứa logic xử lý chính của hệ thống

👉 Thiết kế này giúp:

* Tách biệt phần chạy và phần xử lý
* Dễ bảo trì
* Dễ mở rộng

---

## 🚀 Clone project

```bash
git clone https://github.com/your-username/OS_PROJECT.git
cd OS_PROJECT
```

---

## ⚙️ Cài đặt

```bash
pip install -r requirements.txt
```

---

## ▶️ Chạy chương trình

```bash
python main.py
```

👉 Chức năng:

* Chạy mô phỏng
* Hiển thị kết quả
* Vẽ biểu đồ

---

## 🧪 Test

### Test thuật toán

```bash
python test/test_algorithms.py
```

---

### Test từ CSV

```bash
python test/test_from_csv.py
```

👉 Đọc từ `input/` và xuất ra `output/`

---

## 🖥️ Chạy GUI

```bash
python CODE/gui/main_window.py
```

---

## 📊 Output

Kết quả lưu tại:

```
output/
```

---

## 📄 Tài liệu

* 📄 Báo cáo: `DOCX/report.docx`
* 📊 Slide: `PPTX/`

---

## 🧠 Kết luận

Dự án mô phỏng trực quan các thuật toán thay thế trang, giúp hiểu rõ cơ chế hoạt động và so sánh hiệu năng giữa các thuật toán.

---
