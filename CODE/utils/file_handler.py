import csv
import os

class CSVInputHandler:
    
    @staticmethod
    def read_csv(filepath):
        CSVInputHandler.validate_format_file(filepath)

        pages = []

        try:
            with open(filepath, mode='r', encoding='utf-8-sig') as file:
                reader = csv.reader(file)

                for row_index, row in enumerate(reader):
                    for item in row:
                        item = item.strip()

                        if item:
                            if not item.isdigit():
                                raise ValueError(
                                    f"Dữ liệu lỗi ở dòng {row_index + 1}: '{item}' không phải là số."
                                )
                            pages.append(int(item))

            if not pages:
                raise ValueError("File CSV rỗng hoặc không có dữ liệu hợp lệ.")

        except Exception as e:
            raise RuntimeError(f"Lỗi khi đọc file CSV: {e}")

        return pages

    @staticmethod
    def validate_format_file(filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Không tìm thấy file: '{filepath}'.")

        if not filepath.lower().endswith('.csv'):
            raise ValueError("Đầu vào phải là file .csv.")

        if os.path.getsize(filepath) == 0:
            raise ValueError("File CSV rỗng.")

import csv
import os

class CSVOutputHandler:

    @staticmethod
    def write_csv(filepath, results):
        """
        Ghi kết quả mô phỏng ra file CSV
        :param filepath: đường dẫn file output
        :param results: list các step từ engine
        """

        try:
            # Tạo thư mục nếu chưa tồn tại
            os.makedirs(os.path.dirname(filepath), exist_ok=True)

            with open(filepath, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                # Header đúng format đề
                writer.writerow(["Step", "Page", "Frames", "Fault"])

                # Ghi từng bước
                for step in results:
                    writer.writerow([
                        step.get("step"),
                        step.get("page"),
                        " ".join(map(str, step.get("frames", []))),
                        step.get("fault")
                    ])

        except Exception as e:
            raise RuntimeError(f"Lỗi khi ghi file CSV: {e}")