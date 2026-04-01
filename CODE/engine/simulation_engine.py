# engine/simulation_engine.py

from algorithms.fifo import FIFO
from algorithms.lru import LRU
from algorithms.opt import OPT


class SimulationEngine:
    """
    Simulation Engine:
    - Tách logic khỏi GUI
    - Quản lý các thuật toán thay trang
    - Hỗ trợ chạy full và step-by-step
    """

    def __init__(self):
        self.algorithms = {
            "FIFO": FIFO(),
            "LRU": LRU(),
            "OPT": OPT()
        }

    # =========================
    # VALIDATION
    # =========================
    def validate_input(self, ref_list, frame_count):
        if not isinstance(ref_list, list) or len(ref_list) == 0:
            raise ValueError("Reference string must be a non-empty list")

        if frame_count <= 0:
            raise ValueError("Frame count must be greater than 0")

        if not all(isinstance(x, int) for x in ref_list):
            raise ValueError("Reference string must contain integers only")

    # =========================
    # GET ALGORITHM
    # =========================
    def _get_algorithm(self, name):
        if name not in self.algorithms:
            raise ValueError(f"Unsupported algorithm: {name}")
        return self.algorithms[name]

    # =========================
    # 3.2 RUN FULL SIMULATION
    # =========================
    def run(self, algorithm_name, ref_list, frame_count):
        self.validate_input(ref_list, frame_count)

        algo = self._get_algorithm(algorithm_name)
        results = algo.simulate(ref_list, frame_count)

        total_faults = sum(1 for step in results if step["fault"])

        return {
            "algorithm": algorithm_name,
            "frame_count": frame_count,
            "reference_string": ref_list,
            "results": results,
            "total_faults": total_faults
        }

    # =========================
    # RUN ALL (BONUS)
    # =========================
    def run_all(self, ref_list, frame_count):
        self.validate_input(ref_list, frame_count)

        comparison = {}

        for name in self.algorithms:
            result = self.run(name, ref_list, frame_count)

            comparison[name] = {
                "faults": result["total_faults"],
                "results": result["results"]
            }

        return comparison

    # =========================
    # 3.4 STEP MODE (GENERATOR)
    # =========================
    def step_mode(self, algorithm_name, ref_list, frame_count):
        self.validate_input(ref_list, frame_count)

        algo = self._get_algorithm(algorithm_name)
        results = algo.simulate(ref_list, frame_count)

        for step in results:
            yield step