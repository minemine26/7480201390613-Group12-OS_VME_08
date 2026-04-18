# 🖥️ ĐỒ ÁN HỆ ĐIỀU HÀNH

## MÔ PHỎNG THUẬT TOÁN THAY THẾ TRANG (PAGE REPLACEMENT)

**Project Name:** Virtual Memory Management Simulation
**Project Code:** OS_VME_08

---

## 👥 1. Thành viên thực hiện

| STT | Họ và tên             | MSSV         |
| --- | --------------------- | ------------ |
| 1   | Trần Ngọc Mai         | 089305019922 |
| 2   | Nguyễn Đoàn Thành Đạt | 033206000242 |
| 3   | Nguyễn Văn Minh Đức   | 066206007328 |

---

## 📌 2. Giới thiệu đề tài

Trong hệ điều hành, bộ nhớ ảo (Virtual Memory) giúp mở rộng không gian bộ nhớ bằng cách sử dụng ổ đĩa. Khi một trang không tồn tại trong bộ nhớ vật lý, hệ thống xảy ra **page fault** và cần chọn một trang để thay thế.

Đồ án này mô phỏng các thuật toán thay thế trang:

* FIFO (First-In First-Out)
* LRU (Least Recently Used)
* OPT (Optimal Algorithm)

Hệ thống hỗ trợ mô phỏng từng bước, so sánh thuật toán, xuất file CSV và hiển thị trực quan qua GUI.

---

## 🎯 3. Mục tiêu

* Mô phỏng chính xác thuật toán thay thế trang
* So sánh hiệu năng giữa FIFO, LRU, OPT
* Hỗ trợ nhiều test case từ CSV
* Xây dựng GUI trực quan
* Thiết kế hệ thống theo hướng modular

---

## 🧠 4. Kiến trúc hệ thống

Hệ thống được thiết kế theo mô hình phân lớp:

```id="m0sm5h"
User → main.py → main_logic.py → SimulationEngine → Algorithms → Output
```

### 🔹 Thành phần chính

* **main.py (root)**
  → Điều khiển menu toàn hệ thống

* **main_logic.py**
  → Xử lý simulation (đọc CSV, chạy nhiều test case)

* **SimulationEngine**
  → Điều phối thuật toán, chuẩn hóa kết quả

* **Algorithms (FIFO, LRU, OPT)**
  → Cài đặt logic thay thế trang

* **GUI (main_window.py)**
  → Hiển thị trực quan

* **Utils**
  → Xử lý CSV và biểu đồ

* **Test**
  → Kiểm thử hệ thống

---

## 📁 5. Cấu trúc project

```id="n1p3w0"
OS_PROJECT/
│
├── main.py                  # Entry point
│
├── CODE/
│   ├── main_logic.py        # Core simulation
│   ├── algorithms/          # FIFO, LRU, OPT
│   ├── engine/              # Simulation engine
│   ├── gui/                 # GUI
│   ├── utils/               # CSV + chart
│   └── test/                # Testing
│
├── EXTRA/
│   ├── input/               # input.csv
│   └── output/              # kết quả
│
├── DOCX/
├── PPTX/
```

---

## ⚙️ 6. Hướng dẫn cài đặt

### Bước 1: Clone project

```bash id="8a2r0r"
git clone <repo>
cd OS_PROJECT
```

---

### Bước 2: Cài thư viện

```bash id="0ztz3l"
pip install -r requirements.txt
```

Nếu lỗi:

```bash id="4dtxk3"
python -m pip install -r requirements.txt
```

---

### Bước 3: Kiểm tra

```bash id="07fyx3"
python --version
```

---

## ▶️ 7. Hướng dẫn sử dụng

```bash id="z9ndz3"
python main.py
```

Menu:

* 1 → Simulation
* 2 → GUI
* 3 → Test Algorithms
* 4 → Test CSV

---

## 🧪 8. Simulation (CLI)

* Đọc nhiều test case từ CSV
* Chạy FIFO, LRU, OPT
* In kết quả từng bước
* Hiển thị tổng số page fault

---

## 🖥️ 9. GUI (ĐÃ FIX VÀ HOÀN THIỆN)

GUI là phần quan trọng của hệ thống với các chức năng:

### 🔹 Tính năng

* Run simulation
* Step từng bước
* Auto play
* Reset
* Export kết quả

---

### 🔹 Multi Test Case (ĐÃ FIX)

Hệ thống GUI đã được cải tiến:

* Hỗ trợ nhiều test case từ CSV
* Có thể chuyển qua lại giữa các test case
* Mỗi test case giữ trạng thái riêng

👉 Đây là điểm nâng cấp quan trọng so với phiên bản ban đầu

---

### 🔹 Đồng bộ với engine

GUI sử dụng trực tiếp SimulationEngine → đảm bảo:

* Kết quả chính xác
* Không duplicate logic

---

## 📊 10. Input / Output

### Input

```id="rs0lwd"
EXTRA/input/input.csv
```

Format:

```id="3zjzfy"
frame,ref
3,7 0 1 2 0 3 0 4
```

---

### Output

```id="3tfd4c"
EXTRA/output/
```

Bao gồm:

* testX_fifo.csv
* testX_lru.csv
* testX_opt.csv
* comparison.csv

---

## 🧪 11. Kiểm thử

### 🔹 Test thuật toán

```bash id="i8k1vt"
python CODE/test/test_algorithms.py
```

---

### 🔹 Test CSV

```bash id="j0j9vd"
python CODE/test/test_from_csv.py
```

Chức năng:

* Chạy nhiều test case
* Export kết quả
* So sánh thuật toán

---

## 📈 12. Kết quả và đánh giá

Kết quả thực nghiệm:

```id="z0q2b6"
OPT ≤ LRU ≤ FIFO
```

---

### 🔹 Nhận xét

* FIFO: đơn giản nhưng kém hiệu quả
* LRU: cải thiện đáng kể
* OPT: tối ưu nhất

---

### 🔹 Đánh giá hệ thống

* Hoạt động đúng lý thuyết
* Có kiểm thử
* GUI trực quan
* Hỗ trợ multi-test case

---

## ⚠️ 13. Các lỗi đã gặp và đã fix

### ❌ Lỗi ban đầu

* GUI chỉ chạy được 1 test case
* Lỗi import path (`CODE.xxx`)
* Không export được CSV từ GUI
* Xung đột giữa main root và main_logic
* Test CSV không hoạt động do thiếu function

---

### ✅ Đã khắc phục

* ✔ Fix path import toàn project
* ✔ Chuẩn hóa kiến trúc (main root + main_logic)
* ✔ Thêm `export_all_algorithms`
* ✔ GUI hỗ trợ multi test case
* ✔ Đồng bộ engine giữa CLI và GUI
* ✔ Export CSV hoạt động đúng

---

## 🚀 14. Hướng phát triển

* Thêm thuật toán LFU, Clock
* Cải thiện animation GUI
* Tích hợp biểu đồ trực tiếp
* Hỗ trợ nhập dữ liệu từ GUI

---

## 🧠 15. Kết luận

Đồ án đã xây dựng thành công hệ thống mô phỏng thuật toán thay thế trang với:

* Kiến trúc rõ ràng
* Code modular
* GUI trực quan
* Hỗ trợ multi-test case

Hệ thống giúp hiểu sâu hơn về cơ chế quản lý bộ nhớ trong hệ điều hành.

---
