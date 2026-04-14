import matplotlib.pyplot as plt


class ChartHandler:
    @staticmethod
    def plot_page_fault_comparison(compare_result):
        plt.close("all")

        algorithms = list(compare_result.keys())
        faults = [compare_result[name]["faults"] for name in algorithms]

        plt.figure(figsize=(8, 5))
        plt.bar(algorithms, faults)
        plt.title("Page Fault Comparison")
        plt.xlabel("Algorithm")
        plt.ylabel("Total Page Faults")
        plt.grid(axis="y", linestyle="--", alpha=0.6)
        plt.tight_layout()

    @staticmethod
    def plot_cumulative_faults(compare_result):
        plt.figure(figsize=(10, 6))

        # DEBUG để biết chắc file mới đang được chạy
        print(">>> NEW CHART_HANDLER LOADED <<<")

        styles = {
            "FIFO": {"linestyle": "-", "marker": "o"},
            "LRU": {"linestyle": "--", "marker": "s"},
            "OPT": {"linestyle": ":", "marker": "^"},
        }

        draw_order = ["FIFO", "OPT", "LRU"]

        for algo_name in draw_order:
            data = compare_result[algo_name]
            results = data["results"]

            steps = []
            cumulative_faults = []
            fault_count = 0

            for step_data in results:
                steps.append(step_data["step"])
                if step_data["fault"]:
                    fault_count += 1
                cumulative_faults.append(fault_count)

            # tách đường rõ hơn
            if algo_name == "OPT":
                cumulative_faults = [x - 0.2 for x in cumulative_faults]
            elif algo_name == "LRU":
                cumulative_faults = [x + 0.2 for x in cumulative_faults]

            plt.plot(
                steps,
                cumulative_faults,
                label=algo_name,
                linestyle=styles[algo_name]["linestyle"],
                marker=styles[algo_name]["marker"],
                linewidth=2.5,
                markersize=8
            )

        plt.title("Cumulative Page Faults Comparison")
        plt.xlabel("Step")
        plt.ylabel("Cumulative Faults")
        plt.legend()
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.tight_layout()

    @staticmethod
    def show_all():
        plt.show()