import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os
import sys

# ===== FIX PATH =====
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

# ===== IMPORT =====
from engine.simulation_engine import SimulationEngine
from utils.file_handler import CSVHandler


class PageReplacementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Page Replacement Simulator")
        self.root.geometry("900x600")

        self.engine = SimulationEngine()
        self.file_path = None
        self.steps = []
        self.current_step = 0

        self.build_ui()

    # ================= UI =================
    def build_ui(self):
        # ===== FILE =====
        top = tk.Frame(self.root)
        top.pack(pady=5)

        self.file_label = tk.Label(top, text="No file selected", width=50, anchor="w")
        self.file_label.pack(side=tk.LEFT, padx=5)

        tk.Button(top, text="Choose CSV", command=self.choose_file).pack(side=tk.LEFT)

        # ===== CONFIG =====
        config = tk.Frame(self.root)
        config.pack(pady=5)

        tk.Label(config, text="Frame:").pack(side=tk.LEFT)
        self.frame_entry = tk.Entry(config, width=5)
        self.frame_entry.insert(0, "3")
        self.frame_entry.pack(side=tk.LEFT, padx=5)

        tk.Label(config, text="Algorithm:").pack(side=tk.LEFT)
        self.algo_var = tk.StringVar(value="FIFO")
        ttk.Combobox(
            config,
            textvariable=self.algo_var,
            values=["FIFO", "LRU", "OPT"],
            state="readonly",
            width=10
        ).pack(side=tk.LEFT, padx=5)

        # ===== INFO =====
        self.info_label = tk.Label(self.root, text="Reference String:")
        self.info_label.pack(pady=5)

        # ===== BUTTON =====
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="RUN", bg="green", fg="white", width=10, command=self.run_simulation).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="STEP", bg="blue", fg="white", width=10, command=self.run_step).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="RESET", bg="red", fg="white", width=10, command=self.reset).pack(side=tk.LEFT, padx=5)

        # ===== TABLE =====
        columns = ("Step", "Page", "Frames", "Fault")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=120)

        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # ===== RESULT =====
        self.result_label = tk.Label(self.root, text="Total Faults: 0")
        self.result_label.pack()

    # ================= LOGIC =================
    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.file_path = file_path
            self.file_label.config(text=os.path.basename(file_path))

    def run_simulation(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please choose CSV file")
            return

        try:
            # ===== validate frame =====
            try:
                frame_count = int(self.frame_entry.get())
                if frame_count <= 0:
                    raise ValueError()
            except:
                messagebox.showerror("Error", "Frame không hợp lệ")
                return

            data = CSVHandler.read_csv(self.file_path)

            # ===== FIX MULTI INPUT =====
            if isinstance(data, list) and isinstance(data[0], dict):
                case = data[0]
                ref_list = case["ref"]
                frame_count = case["frame"]
            else:
                ref_list = data

            # ===== SHOW INFO =====
            self.info_label.config(
                text=f"Reference String: {' '.join(map(str, ref_list))} | Frame: {frame_count}"
            )

            result = self.engine.run(self.algo_var.get(), ref_list, frame_count)

            self.steps = result["results"]
            self.current_step = 0

            self.display_all()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_all(self):
        self.tree.delete(*self.tree.get_children())

        for step in self.steps:
            self.tree.insert("", tk.END, values=(
                step["step"],
                step["page"],
                " | ".join(map(str, step["frames"])),
                step["fault"]
            ))

        faults = sum(1 for s in self.steps if s["fault"])
        self.result_label.config(text=f"Total Faults: {faults}")

    def run_step(self):
        if not self.steps:
            messagebox.showinfo("Info", "Run simulation first")
            return

        if self.current_step == 0:
            self.tree.delete(*self.tree.get_children())

        if self.current_step >= len(self.steps):
            return

        step = self.steps[self.current_step]

        self.tree.insert("", tk.END, values=(
            step["step"],
            step["page"],
            " | ".join(map(str, step["frames"])),
            step["fault"]
        ))

        self.current_step += 1

        faults = sum(1 for s in self.steps[:self.current_step] if s["fault"])
        self.result_label.config(text=f"Total Faults: {faults}")

    def reset(self):
        self.tree.delete(*self.tree.get_children())
        self.result_label.config(text="Total Faults: 0")
        self.info_label.config(text="Reference String:")
        self.current_step = 0
        self.steps = []


# ================= RUN =================
if __name__ == "__main__":
    root = tk.Tk()
    app = PageReplacementGUI(root)
    root.mainloop()