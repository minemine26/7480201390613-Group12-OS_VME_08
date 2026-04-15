import os
from engine.simulation_engine import SimulationEngine
from utils.file_handler import CSVHandler


def main():
    print("=== RUN SIMULATION ===")

    ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    input_path = os.path.join(ROOT_DIR, "EXTRA", "input", "input.csv")

    # ===== LOAD DATA =====
    try:
        test_cases = CSVHandler.read_csv(input_path)
    except Exception as e:
        print("❌ Lỗi đọc CSV:", e)
        return

    if not test_cases:
        print("❌ Không có test case")
        return

    engine = SimulationEngine()

    # ===== RUN =====
    for i, case in enumerate(test_cases):
        print(f"\n========== TEST CASE {i+1} ==========")

        ref_list = case["ref"]
        frame = case["frame"]

        print(f"Reference: {ref_list}")
        print(f"Frame: {frame}")

        for algo in ["FIFO", "LRU", "OPT"]:
            result = engine.run(algo, ref_list, frame)

            print(f"\n--- {algo} ---")
            print(f"Total Faults: {result['total_faults']}")

            for step in result["results"]:
                print(
                    f"Step {step['step']:2} | "
                    f"Page: {step['page']:2} | "
                    f"Frames: {step['frames']} | "
                    f"Fault: {step['fault']}"
                )

    print("\n=== DONE SIMULATION ===")

def export_all_algorithms():
    import os
    from utils.file_handler import CSVHandler
    from engine.simulation_engine import SimulationEngine

    ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    input_path = os.path.join(ROOT_DIR, "EXTRA", "input", "input.csv")
    output_dir = os.path.join(ROOT_DIR, "EXTRA", "output")

    os.makedirs(output_dir, exist_ok=True)

    test_cases = CSVHandler.read_csv(input_path)
    engine = SimulationEngine()

    for i, case in enumerate(test_cases):
        ref = case["ref"]
        frame = case["frame"]

        print(f"\n=== TEST {i+1} ===")

        for algo in ["FIFO", "LRU", "OPT"]:
            result = engine.run(algo, ref, frame)

            output_path = os.path.join(
                output_dir, f"test{i+1}_{algo.lower()}.csv"
            )

            CSVHandler.write_csv(output_path, result["results"])

            print(f"{algo}: {result['total_faults']} faults")

    print("\n✅ Export DONE")