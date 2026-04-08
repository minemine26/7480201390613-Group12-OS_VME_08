from algorithms import FIFO, LRU, OPT
from engine import SimulationEngine
from utils.file_handler import CSVHandler


def print_result(name, result):
    print(f"\n=== {name} ===")

    for step in result:
        print(
            f"Step {step['step']:2} | "
            f"Page: {step['page']:2} | "
            f"Frames: {step['frames']} | "
            f"Fault: {step['fault']}"
        )

    total_faults = sum(1 for r in result if r["fault"])
    print(f"Total Page Faults: {total_faults}")


# ================= DEMO ALGORITHMS =================
def demo_algorithms():
    print("\n=== DEMO ALGORITHMS ===")

    ref_list = [7, 0, 1, 2, 0, 3, 0, 4]
    frame_count = 3

    fifo = FIFO()
    lru = LRU()
    opt = OPT()

    print_result("FIFO", fifo.simulate(ref_list, frame_count))
    print_result("LRU", lru.simulate(ref_list, frame_count))
    print_result("OPT", opt.simulate(ref_list, frame_count))


# ================= TEST ENGINE =================
def test_engine():
    print("\n=== TEST SIMULATION ENGINE ===")

    engine = SimulationEngine()
    ref_list = [7, 0, 1, 2, 0, 3, 0, 4]
    frame_count = 3

    result = engine.run("LRU", ref_list, frame_count)

    print("Algorithm:", result["algorithm"])
    print("Total faults:", result["total_faults"])
    print("First step:", result["results"][0])


# ================= TEST CSV =================
def test_csv():
    print("\n=== TEST CSV → OUTPUT ===")

    # ✅ Input (absolute path chuẩn)
    input_path = r"C:\Users\Asus\Desktop\OS_Project\input\input.csv"

    # ✅ Output
    output_path = r"C:\Users\Asus\Desktop\OS_Project\output\result.csv"

    try:
        # 1. Đọc CSV
        ref_list = CSVHandler.read_csv(input_path)
        frame_count = 3

        print("Đọc CSV thành công:", ref_list)

        # 2. Chạy engine
        engine = SimulationEngine()
        result = engine.run("LRU", ref_list, frame_count)

        # 3. Ghi output CSV
        CSVHandler.write_csv(output_path, result["results"])

        print("Xuất file CSV thành công!")

    except Exception as e:
        print("Lỗi:", e)


# ================= MAIN =================
def main():
    print("=== PAGE REPLACEMENT SIMULATOR ===")

    demo_algorithms()
    test_engine()
    test_csv()


if __name__ == "__main__":
    main()