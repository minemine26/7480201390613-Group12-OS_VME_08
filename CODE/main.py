import os
import sys

CURRENT_DIR = os.path.dirname(__file__)
sys.path.append(CURRENT_DIR)

from algorithms import FIFO, LRU, OPT
from engine import SimulationEngine
from utils.file_handler import CSVHandler
import os


# ================= PRINT =================
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


# ================= DEMO =================
def demo_algorithms():
    print("\n=== DEMO ALGORITHMS ===")

    ref_list = [7, 0, 1, 2, 0, 3, 0, 4]
    frame_count = 3

    print_result("FIFO", FIFO().simulate(ref_list, frame_count))
    print_result("LRU", LRU().simulate(ref_list, frame_count))
    print_result("OPT", OPT().simulate(ref_list, frame_count))


# ================= ENGINE =================
def test_engine():
    print("\n=== TEST SIMULATION ENGINE ===")

    engine = SimulationEngine()
    ref_list = [7, 0, 1, 2, 0, 3, 0, 4]

    result = engine.run("LRU", ref_list, 3)

    print("Algorithm:", result["algorithm"])
    print("Total faults:", result["total_faults"])


# ================= BUILD RANKING =================
def build_ranking(results_map):
    sorted_algos = sorted(results_map.items(), key=lambda x: x[1])

    labels = ["BEST", "BETTER", "WORST"]
    ranking = {}

    for i, (algo, _) in enumerate(sorted_algos):
        ranking[algo] = labels[i]

    return ranking


# # ================= EXPORT =================
# def export_all_algorithms():
#     print("\n=== EXPORT ALL ALGORITHMS ===")

#     BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
#     input_path = os.path.join(BASE_DIR, "input", "input.csv")
#     output_dir = os.path.join(BASE_DIR, "output")

#     try:
#         test_cases = CSVHandler.read_csv(input_path)
#         engine = SimulationEngine()

#         for i, case in enumerate(test_cases):
#             frame_count = case["frame"]
#             ref_list = case["ref"]

#             print(f"\n=== TEST CASE {i+1} ===")

#             results_map = {}

#             for algo in ["FIFO", "LRU", "OPT"]:
#                 result = engine.run(algo, ref_list, frame_count)

#                 faults = result["total_faults"]
#                 results_map[algo] = faults

#                 print(f"{algo}: {faults} faults")

#                 output_path = os.path.join(
#                     output_dir, f"test{i+1}_{algo.lower()}.csv"
#                 )
#                 CSVHandler.write_csv(output_path, result["results"])

#             ranking = build_ranking(results_map)

#             print("\n--- Ranking ---")
#             for algo in ["FIFO", "LRU", "OPT"]:
#                 print(f"{algo}: {ranking[algo]}")

#         print("\n✅ Đã export tất cả test cases")

#     except Exception as e:
#         print("❌ Lỗi:", e)


# ================= MAIN =================
def main():
    print("=== PAGE REPLACEMENT SIMULATOR ===")

    demo_algorithms()
    test_engine()
    # export_all_algorithms()


if __name__ == "__main__":
    main()

    
    
    
#================ Chart Handler =================
from engine import SimulationEngine
from utils.chart_handler import ChartHandler
import matplotlib.pyplot as plt


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


def print_comparison(compare):
    print("\n=== COMPARISON ===")
    for name, data in compare.items():
        print(f"{name}: {data['faults']} faults")


def demo_algorithms(engine, ref_list, frame_count):
    print("\n=== DEMO ALGORITHMS ===")
    for algo in ["FIFO", "LRU", "OPT"]:
        result = engine.run(algo, ref_list, frame_count)
        print_result(result)


def test_engine(engine, ref_list, frame_count):
    print("\n=== TEST SIMULATION ENGINE ===")
    result = engine.run("LRU", ref_list, frame_count)
    print("Algorithm:", result["algorithm"])
    print("Total faults:", result["total_faults"])


def draw_charts(engine, ref_list, frame_count):
    print("\n=== DRAW CHARTS ===")

    compare = engine.run_all(ref_list, frame_count)
    print_comparison(compare)

    fifo_result = engine.run("FIFO", ref_list, frame_count)
    lru_result = engine.run("LRU", ref_list, frame_count)
    opt_result = engine.run("OPT", ref_list, frame_count)

    # 7.1 Biểu đồ cột so sánh faults
    ChartHandler.plot_fault_comparison(compare)

    # 7.2 Biểu đồ cumulative faults riêng từng thuật toán
    ChartHandler.plot_cumulative_faults(fifo_result["results"], "FIFO")
    ChartHandler.plot_cumulative_faults(lru_result["results"], "LRU")
    ChartHandler.plot_cumulative_faults(opt_result["results"], "OPT")

    # Bonus: gộp 3 thuật toán trên cùng 1 biểu đồ
    ChartHandler.plot_all_cumulative_faults({
        "FIFO": fifo_result["results"],
        "LRU": lru_result["results"],
        "OPT": opt_result["results"]
    })

    # Hiển thị tất cả đồ thị cùng lúc
    plt.show()


def main():
    print("=== PAGE REPLACEMENT SIMULATOR ===")

    engine = SimulationEngine()

    ref_list = [7, 0, 1, 2, 0, 3, 0, 4]
    frame_count = 3

    demo_algorithms(engine, ref_list, frame_count)
    test_engine(engine, ref_list, frame_count)
    draw_charts(engine, ref_list, frame_count)


if __name__ == "__main__":
    main()
    engine = SimulationEngine()

    ref_list = [7, 0, 1, 2, 0, 3, 0, 4]
    frame_count = 3

    # Chạy tất cả thuật toán
    compare = engine.run_all(ref_list, frame_count)

    # 7.1 Vẽ biểu đồ cột so sánh faults
    ChartHandler.plot_fault_comparison(compare)

    # 7.2 Vẽ cumulative faults cho từng thuật toán
    fifo_result = engine.run("FIFO", ref_list, frame_count)
    lru_result = engine.run("LRU", ref_list, frame_count)
    opt_result = engine.run("OPT", ref_list, frame_count)

    ChartHandler.plot_cumulative_faults(fifo_result["results"], "FIFO")
    ChartHandler.plot_cumulative_faults(lru_result["results"], "LRU")
    ChartHandler.plot_cumulative_faults(opt_result["results"], "OPT")