import csv
import os
import sys
import re

# ===== FIX PATH =====
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

from CODE.main import export_all_algorithms

OUTPUT_DIR = os.path.join(BASE_DIR, "output")


# ================= READ CSV =================
def read_csv(filepath):
    with open(filepath, mode='r', encoding='utf-8') as file:
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

        ranking = {
            algo: labels[i]
            for i, (algo, _) in enumerate(sorted_algos)
        }

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

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Test", "Algorithm", "Faults", "Status"])
        writer.writerows(summary)

    print("\n✅ Exported comparison.csv")


# ================= MAIN =================
def main():
    print("=== AUTO EXPORT + MULTI TEST ===")

    # 1. generate
    export_all_algorithms()

    # 2. load
    all_results = load_all_faults()
    if all_results is None:
        return

    # 3. test từng case
    for test_id, faults_map in all_results.items():
        test_theoretical_correctness(test_id, faults_map)

    # 4. summary
    summary = build_summary(all_results)

    # 5. export
    export_comparison(summary)


if __name__ == "__main__":
    main()

import os
from CODE.engine.simulation_engine import SimulationEngine
from CODE.utils.file_handler import CSVHandler


def main():
    print("\n=== AUTO EXPORT + MULTI TEST ===")

    # 1. Gọi logic chính từ CODE/main.py
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