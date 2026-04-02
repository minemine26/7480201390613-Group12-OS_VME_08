import csv
import os

class CSVInputHandler:
    
    @staticmethod
    def read_csv(filepath):
        # Rào lỗi, tránh crash
        CSVInputHandler.validate_format_file(filepath)
        pages = []
        try:
            with open(filepath, mode='r', encoding='utf-8-sig') as file:
                reader = csv.reader(file)
                for row_index, row in enumerate(reader):
                    for item in row:
                        item = item.strip()
                        if item:
                            # Chặn thêm lỗi rác dữ liệu bên trong file
                            if not item.isdigit():
                                raise ValueError(f"Dữ liệu lỗi ở dòng {row_index + 1}: '{item}' không phải là số.")
                            pages.append(int(item))
        except Exception as e:
            # Raise error nếu có lỗi phát sinh trong quá trình đọc
            raise RuntimeError(f"Lỗi khi đọc file CSV: {e}")
            
        return pages

    @staticmethod
    def validate_format_file(filepath):
        # Kiểm tra file có tồn tại không
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Lỗi: Không tìm thấy file tại '{filepath}'.")
            
        # Kiểm tra đúng đuôi .csv không
        if not filepath.lower().endswith('.csv'):
            raise ValueError("Lỗi định dạng: Đầu vào bắt buộc phải là file .csv!")