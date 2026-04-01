# 🖥️ Đồ án Hệ Điều Hành – Nhóm 12

**Project Name:** Demo Virtual Memory Management Algorithm: LRU, FIFO và OPT
**Project Code:** OS_VME_08

##  Danh sách thành viên Nhóm 12
| STT | Họ và tên             | Mã số sinh viên |
| --- | --------------------- | --------------- |
| 1   | Trần Ngọc Mai         | 089305019922    |
| 2   | Nguyễn Đoàn Thành Đạt | 033206000242    |
| 3   | Nguyễn Văn Minh Đức   | 066206007328    |


## 📁 Repository Structure (Cấu trúc thư mục)
- `CODE/`: Chứa toàn bộ mã nguồn (Source code) Python của ứng dụng.
- `DOCX/`: Chứa file báo cáo định dạng Word tổng kết quá trình làm đồ án, các thuật toán và bài học kinh nghiệm.
- `Extra/`: Chứa các tài liệu bổ sung, bằng chứng kiểm thử (video demo, ảnh chụp màn hình).
- `PPTX/`: Chứa file slide thuyết trình PowerPoint.
- `input/`: Chứa các file `.csv` dữ liệu mẫu đầu vào (chuỗi tham chiếu, số khung trang).
- `output/`: Chứa các file `.csv` kết quả xuất ra sau khi chạy mô phỏng thuật toán.

## 🛠️ Technologies Used (Công nghệ dự kiến sử dụng)

- **Programming Language:** Python 3.8+
- **GUI Framework:** PyQt5
- **Data Handling:** pandas, csv (Python built-in)
- **Visualization:** matplotlib (cho biểu đồ so sánh)
- **Version Control:** Git, GitHub

##  Mô tả dự án

Đây là đồ án môn **Hệ Điều Hành (Operating System)** với mục tiêu xây dựng một ứng dụng có **giao diện đồ họa (GUI)** nhằm mô phỏng và trực quan hóa các thuật toán thay thế trang trong **quản lý bộ nhớ ảo (Virtual Memory Management)**.

Các thuật toán được triển khai bao gồm:

* **FIFO (First-In, First-Out):** Thay thế trang vào trước ra trước
* **LRU (Least Recently Used):** Thay thế trang ít được sử dụng gần đây nhất
* **OPT (Optimal Page Replacement):** Thay thế trang có lần sử dụng tiếp theo xa nhất

---

##  Chức năng chính

*  Đọc dữ liệu đầu vào từ file `.csv`:

  * Chuỗi tham chiếu (reference string)
  * Số khung trang (frame count)

*  Mô phỏng thuật toán:

  * Hiển thị **từng bước** thay thế trang
  * Theo dõi trạng thái khung trang theo thời gian
  * Xác định và đánh dấu **Page Fault**

*  Hiển thị kết quả:

  * Bảng dữ liệu (Data Grid)
  * Tổng số Page Fault của từng thuật toán
  * So sánh giữa các thuật toán

*  Xuất kết quả:

  * Lưu kết quả chi tiết ra file `.csv`

*  (Nâng cao):

  * Biểu đồ so sánh số Page Fault
  * Biểu đồ xu hướng tích lũy lỗi trang

---

##  Công nghệ sử dụng

* **Ngôn ngữ lập trình:** Python 3.8+
* **Giao diện:** PyQt5
* **Xử lý dữ liệu:** csv, pandas
* **Trực quan hóa:** matplotlib
* **Quản lý mã nguồn:** Git, GitHub

---

##  Cấu trúc thư mục

```
OS_PROJECT/
│
├── CODE/
│   ├── main.py                  # Điểm bắt đầu chương trình
│
│   ├── algorithms/              # Các thuật toán thay thế trang
│   │   ├── base.py
│   │   ├── fifo.py
│   │   ├── lru.py
│   │   └── opt.py
│
│   ├── engine/                  # Điều phối mô phỏng
│   │   └── simulation_engine.py
│
│   ├── gui/                     # Giao diện PyQt5
│   │   └── main_window.py
│
│   ├── models/                  # Cấu trúc dữ liệu
│   │   └── simulation_result.py
│
│   ├── utils/                   # Xử lý file CSV
│   │   └── file_handler.py
│
├── input/                       # File CSV đầu vào
├── output/                      # File CSV kết quả
├── DOCX/                        # Báo cáo Word
├── PPTX/                        # Slide thuyết trình
├── Extra/                       # Tài liệu bổ sung, demo
├── test/                        # Unit test (nếu có)
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

##  Luồng hoạt động của hệ thống

1. Người dùng chọn file `.csv` đầu vào
2. Hệ thống đọc dữ liệu (reference string + frame count)
3. Người dùng chọn thuật toán (FIFO / LRU / OPT)
4. Engine thực hiện mô phỏng theo từng bước
5. Kết quả được trả về bao gồm:

   * Trang được truy cập
   * Trạng thái khung trang
   * Page Fault (Có/Không)
6. Giao diện hiển thị kết quả dưới dạng bảng
7. (Tuỳ chọn) Xuất kết quả ra file `.csv` hoặc vẽ biểu đồ

---

##  Định dạng file đầu vào

File CSV cần có cấu trúc:

```
reference_string,frame_count
7,0,1,2,0,3,0,4
3
```

---

##  Định dạng file đầu ra

```
Algorithm,Step,Page,Frame_State,Page_Fault
FIFO,1,7,[7],True
FIFO,2,0,[7,0],True
...
```

---

## ▶ Hướng dẫn chạy chương trình

### 1. Tạo môi trường ảo

```bash
python -m venv .venv
```

### 2. Kích hoạt môi trường

```bash
.\.venv\Scripts\activate
```

### 3. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

### 4. Chạy chương trình

```bash
python CODE/main.py
```

---

##  Ghi chú

* Đảm bảo file `.csv` đúng định dạng trước khi chạy
* Không sử dụng nhiều môi trường ảo cùng lúc
* Khuyến nghị sử dụng Python 3.8 trở lên

---

##  Kết luận

Dự án giúp minh họa rõ ràng cách hoạt động của các thuật toán thay thế trang trong hệ điều hành, đồng thời cung cấp công cụ trực quan để so sánh hiệu năng giữa các thuật toán.

Đây là nền tảng để mở rộng thêm các thuật toán khác như **LFU, MFU** hoặc nâng cấp giao diện trực quan trong tương lai.
