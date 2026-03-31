from algorithms.fifo import FIFO
from algorithms.lru import LRU
from algorithms.opt import OPT
if __name__ == "__main__":
    ref_list = [7, 0, 1, 2, 0, 3, 0, 4]
    frame_count = 3

    # FIFO
    fifo = FIFO()
    fifo_result = fifo.simulate(ref_list, frame_count)

    print("=== FIFO ===")
    for r in fifo_result:
        print(r)

    fifo_faults = sum(1 for r in fifo_result if r["fault"])
    print("Total FIFO faults:", fifo_faults)

    print("\n")

    # LRU
    lru = LRU()
    lru_result = lru.simulate(ref_list, frame_count)

    print("=== LRU ===")
    for r in lru_result:
        print(r)

    lru_faults = sum(1 for r in lru_result if r["fault"])
    print("Total LRU faults:", lru_faults)
    
    print("\n")
    
    #OPT
    opt = OPT()
    opt_result = opt.simulate(ref_list, frame_count)

    print("=== OPT ===")
    for r in opt_result:
        print(r)

    opt_faults = sum(1 for r in opt_result if r["fault"])
    print("Total OPT faults:", opt_faults)