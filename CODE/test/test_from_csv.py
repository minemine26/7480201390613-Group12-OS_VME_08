import csv
import os
import sys
import re

# ===== FIX PATH =====
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CODE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
ROOT_DIR = os.path.abspath(os.path.join(CODE_DIR, ".."))

if CODE_DIR not in sys.path:
    sys.path.append(CODE_DIR)

from main_logic import export_all_algorithms

# Nếu nhóm đã chuyển output vào Extra
OUTPUT_DIR = os.path.join(ROOT_DIR, "Extra", "output")

# Nếu CHƯA chuyển output vào Extra thì dùng dòng này thay dòng trên:
# OUTPUT_DIR = os.path.join(ROOT_DIR, "output")


# ================= READ CSV =================
def read_csv(filepath):
    with open(filepath, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [
            {"fault": str(row["Fault"]).strip().lower() == "true"}
            for row in reader
        ]


# ================= COUNT =================
def count_faults(results):
    return sum(1 for r in results if r["fault"])


# ================= FIND ALL TEST CASES =================
def find_test_cases():
    if not os.path.exists(OUTPUT_DIR):
        print(f"❌ Không tìm thấy thư mục output: {OUTPUT_DIR}")
        return {}

    files = os.listdir(OUTPUT_DIR)
    pattern = re.compile(r"test(\d+)_(fifo|lru|opt)\.csv")

    test_cases = {}

    for f in files:
        match = pattern.match(f.lower())
        if match:
            test_id = int(match.group(1))
            algo = match.group(2).upper()

            if test_id not in test_cases:
                test_cases[test_id] = {}

            test_cases[test_id][algo] = f

    return test_cases


# ================= LOAD ALL TEST =================
def load_all_faults():
    test_cases = find_test_cases()
    if not test_cases:
        return None

    all_results = {}

    for test_id, files in sorted(test_cases.items()):
        faults_map = {}

        for algo in ["FIFO", "LRU", "OPT"]:
            if algo not in files:
                print(f"❌ Missing {algo} in test{test_id}")
                return None

            path = os.path.join(OUTPUT_DIR, files[algo])
            results = read_csv(path)
            faults_map[algo] = count_faults(results)

        all_results[test_id] = faults_map

    return all_results


# ================= TEST =================
def test_theoretical_correctness(test_id, faults_map):
    print(f"\n=== TEST {test_id} ===")

    fifo = faults_map["FIFO"]
    lru = faults_map["LRU"]
    opt = faults_map["OPT"]

    print(f"FIFO: {fifo}")
    print(f"LRU : {lru}")
    print(f"OPT : {opt}")

    if opt <= lru <= fifo:
        print("✅ PASS")
    else:
        print("❌ FAIL")


# ================= BUILD SUMMARY =================
def build_summary(all_results):
    summary = []

    for test_id, faults_map in all_results.items():
        sorted_algos = sorted(faults_map.items(), key=lambda x: x[1])
        labels = ["BEST", "BETTER", "WORST"]

        ranking = {}
        for i, (algo, _) in enumerate(sorted_algos):
            if i < len(labels):
                ranking[algo] = labels[i]
            else:
                ranking[algo] = "UNKNOWN"

        for algo in ["FIFO", "LRU", "OPT"]:
            summary.append([
                f"Test{test_id}",
                algo,
                faults_map[algo],
                ranking[algo]
            ])

    return summary


# ================= EXPORT =================
def export_comparison(summary):
    output_file = os.path.join(OUTPUT_DIR, "comparison.csv")

    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Test", "Algorithm", "Faults", "Status"])
        writer.writerows(summary)

    print("\n✅ Exported comparison.csv")


# ================= MAIN =================
def main():
    print("=== AUTO EXPORT + MULTI TEST ===")

    # 1. Generate output từ main_logic
    export_all_algorithms()

    # 2. Load toàn bộ kết quả
    all_results = load_all_faults()
    if all_results is None:
        print("❌ Không load được dữ liệu")
        return

    print("\n===== KẾT QUẢ TỪNG TEST =====")

    # 3. Test từng case
    for test_id, faults_map in all_results.items():
        test_theoretical_correctness(test_id, faults_map)

    print("\n===== SO SÁNH & XẾP HẠNG =====")

    # 4. Summary
    summary = build_summary(all_results)

    for row in summary:
        print(f"{row[0]} | {row[1]} | Faults: {row[2]} | {row[3]}")

    # 5. Export file tổng hợp
    export_comparison(summary)

    print("\n✅ DONE ALL TESTS")


if __name__ == "__main__":
    main()