import sys
import os


# Thêm đường dẫn tới thư mục CODE
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "CODE")))

from algorithms.fifo import FIFO
from algorithms.lru import LRU
from algorithms.opt import OPT


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

    # Kiểm tra lý thuyết
    if opt_faults <= lru_faults <= fifo_faults:
        print("✅ Đúng lý thuyết: OPT ≤ LRU ≤ FIFO")
    else:
        print("❌ Sai lý thuyết")


# ================= MAIN =================
if __name__ == "__main__":
    test_comparison()