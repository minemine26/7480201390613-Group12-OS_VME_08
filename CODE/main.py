from engine import SimulationEngine
from utils.file_handler import CSVInputHandler, CSVOutputHandler
import os


# ===============================
# HIỂN THỊ KẾT QUẢ
# ===============================
def print_result(result):
    print(f"\n=== {result['algorithm']} ===")
    print(f"Frame count: {result['frame_count']}")
    print(f"Reference string: {result['reference_string']}")
    print("-" * 50)

    for step in result["results"]:
        print(
            f"Step {step['step']:2} | "
            f"Page: {step['page']:2} | "
            f"Frames: {step['frames']} | "
            f"Fault: {step['fault']}"
        )

    print("-" * 50)
    print(f"Total Page Faults: {result['total_faults']}")


# ===============================
# SO SÁNH THUẬT TOÁN
# ===============================
def print_comparison(compare):
    print("\n=== COMPARISON ===")
    for name, data in compare.items():
        print(f"{name}: {data['faults']} faults")


# ===============================
# CHƯƠNG TRÌNH CHÍNH
# ===============================
if __name__ == "__main__":

    # 1. ĐỌC FILE CSV
    try:
        input_path = "input/input.csv"
        ref_list = CSVInputHandler.read_csv(input_path)
    except Exception as e:
        print("Lỗi đọc file CSV:", e)
        exit()

    # 2. CẤU HÌNH FRAME
    frame_count = 3

    # 3. KHỞI TẠO ENGINE
    engine = SimulationEngine()

    # 4. CHẠY TỪNG THUẬT TOÁN
    for algo in ["FIFO", "LRU", "OPT"]:
        result = engine.run(algo, ref_list, frame_count)
        print_result(result)

    # 5. SO SÁNH
    compare = engine.run_all(ref_list, frame_count)
    print_comparison(compare)

    # 6. STEP MODE (TEST)
    print("\n=== STEP MODE (OPT) ===")
    for step in engine.step_mode("OPT", ref_list, frame_count):
        print(step)

    # 7. XUẤT FILE CSV (LRU)
    try:
        output_path = "../output/output.csv"

        # tạo thư mục nếu chưa có
        os.makedirs("output", exist_ok=True)

        output_path = "output/output.csv"
        CSVOutputHandler.write_csv(output_path, result["results"])

        print("\nXuất file CSV thành công!")
        print("File nằm tại:", output_path)

    except Exception as e:
        print("Lỗi ghi file CSV:", e)