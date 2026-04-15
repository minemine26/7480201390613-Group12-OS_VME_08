import sys
import os

# ================= FIX PATH =================
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from algorithms.fifo import FIFO
from algorithms.lru import LRU
from algorithms.opt import OPT
from engine.simulation_engine import SimulationEngine


# ================= COMMON =================
def count_faults(results):
    return sum(1 for step in results if step["fault"])


# ================= FIFO =================
def test_fifo():
    print("\n=== TEST FIFO ===")

    ref_list = [7, 0, 1, 2, 0, 3, 0, 4]
    frame_count = 3
    expected_faults = 7

    fifo = FIFO()
    results = fifo.simulate(ref_list, frame_count)
    actual_faults = count_faults(results)

    print(f"Expected faults: {expected_faults}")
    print(f"Actual faults:   {actual_faults}")

    if actual_faults == expected_faults:
        print("✅ FIFO PASS")
    else:
        print("❌ FIFO FAIL")

    return actual_faults


# ================= LRU =================
def test_lru():
    print("\n=== TEST LRU ===")

    ref_list = [7, 0, 1, 2, 0, 3, 0, 4]
    frame_count = 3
    expected_faults = 6

    lru = LRU()
    results = lru.simulate(ref_list, frame_count)
    actual_faults = count_faults(results)

    print(f"Expected faults: {expected_faults}")
    print(f"Actual faults:   {actual_faults}")

    if actual_faults == expected_faults:
        print("✅ LRU PASS")
    else:
        print("❌ LRU FAIL")

    return actual_faults


# ================= OPT =================
def test_opt():
    print("\n=== TEST OPT ===")

    ref_list = [7, 0, 1, 2, 0, 3, 0, 4]
    frame_count = 3
    expected_faults = 6

    opt = OPT()
    results = opt.simulate(ref_list, frame_count)
    actual_faults = count_faults(results)

    print(f"Expected faults: {expected_faults}")
    print(f"Actual faults:   {actual_faults}")

    if actual_faults == expected_faults:
        print("✅ OPT PASS")
    else:
        print("❌ OPT FAIL")

    return actual_faults


# ================= COMPARISON =================
def test_comparison():
    print("\n=== TEST COMPARISON ===")

    fifo_faults = test_fifo()
    lru_faults = test_lru()
    opt_faults = test_opt()

    print("\n=== RESULT COMPARISON ===")
    print(f"FIFO faults: {fifo_faults}")
    print(f"LRU faults : {lru_faults}")
    print(f"OPT faults : {opt_faults}")

    if opt_faults <= lru_faults <= fifo_faults:
        print("✅ Đúng lý thuyết: OPT ≤ LRU ≤ FIFO")
    else:
        print("❌ Sai lý thuyết")


# ================= ENGINE TEST =================
def test_engine():
    print("\n===== TEST ENGINE =====")

    ref_string = [7, 0, 1, 2, 0, 3, 0, 4]
    frame = 3

    engine = SimulationEngine()

    for algo in ["FIFO", "LRU", "OPT"]:
        result = engine.run(algo, ref_string, frame)
        faults = sum(1 for step in result["results"] if step["fault"])

        print(f"\nAlgorithm: {algo}")
        print(f"Reference: {ref_string}")
        print(f"Frame: {frame}")
        print(f"Total Page Faults: {faults}")

    print("\n===== DONE =====")


# ================= MAIN =================
def main():
    print("===== TEST ALGORITHMS =====")
    test_comparison()
    test_engine()


if __name__ == "__main__":
    main()