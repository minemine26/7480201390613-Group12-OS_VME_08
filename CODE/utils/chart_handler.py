import matplotlib.pyplot as plt


class ChartHandler:
    """
    Xử lý vẽ biểu đồ cho hệ thống mô phỏng thay thế trang
    """

    @staticmethod
    def plot_fault_comparison(compare_result):
        """
        7.1 Bar chart:
        So sánh tổng số page faults giữa FIFO, LRU, OPT
        compare_result có dạng:
        {
            "FIFO": {"faults": 7, "results": [...]},
            "LRU": {"faults": 6, "results": [...]},
            "OPT": {"faults": 6, "results": [...]}
        }
        """
        labels = list(compare_result.keys())
        faults = [compare_result[name]["faults"] for name in labels]

        plt.figure(figsize=(8, 5))
        plt.bar(labels, faults)
        plt.title("Page Fault Comparison")
        plt.xlabel("Algorithm")
        plt.ylabel("Total Page Faults")
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.tight_layout()

    @staticmethod
    def plot_cumulative_faults(results, algorithm_name):
        """
        7.2 Cumulative faults:
        Vẽ đường tăng dần của số page faults theo từng bước
        """
        steps = []
        cumulative_faults = []

        fault_count = 0
        for step in results:
            if step["fault"]:
                fault_count += 1
            steps.append(step["step"])
            cumulative_faults.append(fault_count)

        plt.figure(figsize=(8, 5))
        plt.plot(steps, cumulative_faults, marker="o")
        plt.title(f"Cumulative Page Faults - {algorithm_name}")
        plt.xlabel("Step")
        plt.ylabel("Cumulative Faults")
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.tight_layout()

    @staticmethod
    def plot_all_cumulative_faults(results_map):
        """
        Vẽ cumulative faults của nhiều thuật toán trên cùng một biểu đồ
        results_map có dạng:
        {
            "FIFO": [...],
            "LRU": [...],
            "OPT": [...]
        }
        """
        plt.figure(figsize=(8, 5))

        for algorithm_name, results in results_map.items():
            steps = []
            cumulative_faults = []
            fault_count = 0

            for step in results:
                if step["fault"]:
                    fault_count += 1
                steps.append(step["step"])
                cumulative_faults.append(fault_count)

            plt.plot(steps, cumulative_faults, marker="o", label=algorithm_name)

        plt.title("Cumulative Page Faults Comparison")
        plt.xlabel("Step")
        plt.ylabel("Cumulative Faults")
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.legend()
        plt.tight_layout()