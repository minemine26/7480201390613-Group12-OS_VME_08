from engine.simulation_engine import SimulationEngine

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


def test_single_algorithm(engine, ref_list, frame_count):
    for algo in ["FIFO", "LRU", "OPT"]:
        result = engine.run(algo, ref_list, frame_count)
        print_result(result)


def test_comparison(engine, ref_list, frame_count):
    compare = engine.run_all(ref_list, frame_count)
    print_comparison(compare)


def test_step_mode(engine, ref_list, frame_count):
    print("\n=== STEP MODE (OPT) ===")
    for step in engine.step_mode("OPT", ref_list, frame_count):
        print(step)


if __name__ == "__main__":
    engine = SimulationEngine()

    ref_list = [7, 0, 1, 2, 0, 3, 0, 4]
    frame_count = 3

    test_single_algorithm(engine, ref_list, frame_count)

    test_comparison(engine, ref_list, frame_count)

    test_step_mode(engine, ref_list, frame_count)