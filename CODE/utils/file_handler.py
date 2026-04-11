import csv
import os


class CSVHandler:
    """
    CSV Handler:
    - read_csv: đọc input (multi test)
    - validate_format_file: kiểm tra file
    - write_csv: ghi output
    """

    # ================= READ =================
    @staticmethod
    def read_csv(filepath):
        CSVHandler.validate_format_file(filepath)

        try:
            with open(filepath, mode='r', encoding='utf-8-sig') as file:
                lines = [line.strip() for line in file if line.strip()]

            test_cases = []
            current_frame = None

            for line in lines:
                if line.startswith("#"):
                    continue

                if line.startswith("frame="):
                    current_frame = int(line.split("=")[1])

                elif line.startswith("ref="):
                    ref_str = line.split("=")[1]
                    ref_list = [int(x) for x in ref_str.replace(",", " ").split()]

                    if current_frame is None:
                        raise ValueError("Thiếu frame trước ref")

                    test_cases.append({
                        "frame": current_frame,
                        "ref": ref_list
                    })

                    current_frame = None

            if not test_cases:
                raise ValueError("Không có test case hợp lệ")

            return test_cases

        except Exception as e:
            raise RuntimeError(f"Lỗi đọc CSV: {e}")

    # ================= VALIDATE =================
    @staticmethod
    def validate_format_file(filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Không tìm thấy file: '{filepath}'.")

        if not filepath.lower().endswith('.csv'):
            raise ValueError("Đầu vào phải là file .csv.")

        if os.path.getsize(filepath) == 0:
            raise ValueError("File CSV rỗng.")

    # ================= WRITE =================
    @staticmethod
    def write_csv(filepath, results):
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)

            with open(filepath, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                writer.writerow(["Step", "Page", "Frames", "Fault"])

                for step in results:
                    writer.writerow([
                        step.get("step"),
                        step.get("page"),
                        " ".join(map(str, step.get("frames", []))),
                        step.get("fault")
                    ])

            print(f"Đã ghi file output: {filepath}")

        except Exception as e:
            raise RuntimeError(f"Lỗi khi ghi file CSV: {e}")