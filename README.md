# 🖥️ Operating System Project - Group 12

**Project Name:** Demo Virtual Memory Management algorithm: LRU, FIFO and OPT  
**Project Code:** OS_VME_08  

---

## 👥 Group Members (Danh sách thành viên Nhóm 12)

| STT | Họ và tên      | Mã số sinh viên |
|-----|----------------|------------------|
| 1   | Trần Ngọc Mai  | 089305019922     |

---

## 📖 Project Description (Mô tả dự án)

Dự án này là bài tập lớn môn **Hệ điều hành (Operating System)**. Mục tiêu của dự án là xây dựng một ứng dụng có giao diện đồ họa (GUI) để mô phỏng và trực quan hóa các thuật toán thay thế trang trong quản lý bộ nhớ ảo (Virtual Memory Management), bao gồm:

- **FIFO** (First-In, First-Out)
- **LRU** (Least Recently Used)
- **OPT** (Optimal Page Replacement)

Ứng dụng sẽ đọc chuỗi tham chiếu (reference string) và số khung trang (page frames) từ file `.csv` đầu vào, tiến hành mô phỏng quá trình thay trang, trực quan hóa kết quả lên bảng (Data Grid), tính toán số lượng lỗi trang (Page Faults) và xuất kết quả chi tiết ra file `.csv` đầu ra.

---

## 📁 Repository Structure (Cấu trúc thư mục)

Dự án tuân thủ nghiêm ngặt cấu trúc thư mục được yêu cầu:
OS_Project/
├── CODE/ # Toàn bộ mã nguồn của ứng dụng
│ ├── main.py # Điểm khởi chạy chính
│ ├── algorithms.py # Các thuật toán FIFO, LRU, OPT
│ ├── gui.py # Giao diện đồ họa 
│ ├── file_handler.py # Đọc/ghi file CSV
│ └── simulation_engine.py# Engine chạy mô phỏng
├── DOCX/ # Báo cáo Word
├── Extra/ # Tài liệu bổ sung, CSV mẫu, video demo, ...
├── PPTX/ # Slide thuyết trình PowerPoint
├── input/ # File CSV đầu vào
│ └── input.csv # Dữ liệu mẫu
├── output/ # Kết quả xuất ra
├── .gitignore
├── requirements.txt # Danh sách thư viện cần cài đặt
└── README.md 


> **Lưu ý:** Thư mục `output/` và các file CSV kết quả được đưa vào `.gitignore` để không đẩy lên GitHub.

---

## 🛠️ Technologies Used (Công nghệ dự kiến sử dụng)

- **Programming Language:** Python 3.8+
- **GUI Framework:** PyQt5
- **Data Handling:** pandas, csv (Python built-in)
- **Visualization:** matplotlib (cho biểu đồ so sánh)
- **Version Control:** Git, GitHub

---

