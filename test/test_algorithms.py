import sys
import os

# Fix path
sys.path.append(os.path.abspath("CODE"))

from algorithms.fifo import FIFO
from algorithms.lru import LRU


def test_fifo():
    print("\n=== TEST FIFO ===")

    ref_list = [7, 0, 1, 2, 0, 3, 0, 4]
    frame_count = 3
    expected_faults = 7

    fifo = FIFO()
    result = fifo.simulate(ref_list, frame_count)

    actual_faults = sum(1 for step in result if step["fault"])

    print(f"Expected faults: {expected_faults}")
    print(f"Actual faults:   {actual_faults}")

    if actual_faults == expected_faults:
        print("✅ FIFO PASS")
    else:
        print("❌ FIFO FAIL")


def test_lru():
    print("\n=== TEST LRU ===")

    ref_list = [7, 0, 1, 2, 0, 3, 0, 4]
    frame_count = 3
    expected_faults = 6

    lru = LRU()
    result = lru.simulate(ref_list, frame_count)

    actual_faults = sum(1 for step in result if step["fault"])

    print(f"Expected faults: {expected_faults}")
    print(f"Actual faults:   {actual_faults}")

    if actual_faults == expected_faults:
        print("✅ LRU PASS")
    else:
        print("❌ LRU FAIL")


if __name__ == "__main__":
    test_fifo()
    test_lru()