from algorithms import FIFO, LRU, OPT


class SimulationEngine:


    def __init__(self):
        self.algorithms = {
            "FIFO": FIFO(),
            "LRU": LRU(),
            "OPT": OPT()
        }

  
    def validate_input(self, ref_list, frame_count):
        if not isinstance(ref_list, list) or len(ref_list) == 0:
            raise ValueError("Reference string must be a non-empty list")

        if frame_count <= 0:
            raise ValueError("Frame count must be greater than 0")

        if not all(isinstance(x, int) for x in ref_list):
            raise ValueError("Reference string must contain integers only")


    def _get_algorithm(self, name):
        if name not in self.algorithms:
            raise ValueError(f"Unsupported algorithm: {name}")
        return self.algorithms[name]

   
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


    def step_mode(self, algorithm_name, ref_list, frame_count):
        self.validate_input(ref_list, frame_count)

        algo = self._get_algorithm(algorithm_name)
        results = algo.simulate(ref_list, frame_count)

        for step in results:
            yield step
            
    # lớp trung gian giữa GUI và agorithms
    # lưa chọn, thực thi và chuẩn hóa kết quả 