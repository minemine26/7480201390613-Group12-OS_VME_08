import csv
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

from engine.simulation_engine import SimulationEngine
from utils.file_handler import CSVHandler


class PageReplacementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Page Replacement Simulator")
        self.root.geometry("950x650")

        self.engine = SimulationEngine()

        self.file_path = None
        self.steps = []
        self.current_step = 0

        # ===== MULTI TEST =====
        self.test_cases = []
        self.current_test_index = 0

        self.is_auto_playing = False

        self.build_ui()

    # ================= UI =================
    def build_ui(self):
        top = tk.Frame(self.root)
        top.pack(pady=5)

        self.file_label = tk.Label(top, text="No file selected", width=50, anchor="w")
        self.file_label.pack(side=tk.LEFT, padx=5)

        tk.Button(top, text="Choose CSV", command=self.choose_file).pack(side=tk.LEFT)

        config = tk.Frame(self.root)
        config.pack(pady=5)

        tk.Label(config, text="Frame:").pack(side=tk.LEFT)
        self.frame_entry = tk.Entry(config, width=5)
        self.frame_entry.insert(0, "3")
        self.frame_entry.pack(side=tk.LEFT, padx=5)

        tk.Label(config, text="Algorithm:").pack(side=tk.LEFT)
        self.algo_var = tk.StringVar(value="FIFO")
        ttk.Combobox(config, textvariable=self.algo_var,
                     values=["FIFO", "LRU", "OPT"],
                     state="readonly", width=10).pack(side=tk.LEFT, padx=5)

        self.info_label = tk.Label(self.root, text="Reference String:")
        self.info_label.pack(pady=5)

        # ===== BUTTON =====
        btn = tk.Frame(self.root)
        btn.pack(pady=5)

        tk.Button(btn, text="RUN", bg="green", fg="white", width=10, command=self.run_simulation).pack(side=tk.LEFT, padx=2)
        tk.Button(btn, text="STEP", bg="blue", fg="white", width=10, command=self.run_step).pack(side=tk.LEFT, padx=2)
        tk.Button(btn, text="RESET", bg="red", fg="white", width=10, command=self.reset).pack(side=tk.LEFT, padx=2)

        self.btn_auto = tk.Button(btn, text="AUTO PLAY", bg="purple", fg="white", width=10, command=self.toggle_auto)
        self.btn_auto.pack(side=tk.LEFT, padx=2)

        tk.Button(btn, text="SHOW PROOF", bg="#e67e22", fg="white", command=self.show_proof).pack(side=tk.LEFT, padx=2)
        tk.Button(btn, text="EXPORT", bg="gray", fg="white", command=self.export_csv).pack(side=tk.LEFT, padx=2)
        tk.Button(btn, text="HELP", bg="#f1c40f", command=self.show_help).pack(side=tk.LEFT, padx=2)

        # ===== MULTI TEST =====
        tk.Button(btn, text="<< BACK", bg="#2c3e50", fg="white", command=self.prev_test).pack(side=tk.LEFT, padx=2)
        tk.Button(btn, text="NEXT >>", bg="#2c3e50", fg="white", command=self.next_test).pack(side=tk.LEFT, padx=2)

        # ===== FRAME DISPLAY =====
        self.visual = tk.LabelFrame(self.root, text="Memory (Red=Fault, Green=Hit)")
        self.visual.pack(fill=tk.X, padx=10, pady=5)

        self.frame_box = tk.Frame(self.visual)
        self.frame_box.pack(pady=10)

        # ===== TABLE =====
        cols = ("Step", "Page", "Frames", "Fault")
        self.tree = ttk.Treeview(self.root, columns=cols, show="headings")

        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, anchor="center", width=120)

        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.result_label = tk.Label(self.root, text="Total Faults: 0")
        self.result_label.pack()

    # ================= FILE =================
    def choose_file(self):
        path = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])
        if path:
            self.file_path = path
            self.file_label.config(text=os.path.basename(path))

    # ================= RUN =================
    def run_simulation(self):
        if not self.file_path:
            messagebox.showerror("Error", "Choose CSV first")
            return

        data = CSVHandler.read_csv(self.file_path)

        if isinstance(data, list) and isinstance(data[0], dict):
            self.test_cases = data
        else:
            self.test_cases = [{"ref": data, "frame": int(self.frame_entry.get())}]

        self.current_test_index = 0
        self.run_current_test()

    def run_current_test(self):
        case = self.test_cases[self.current_test_index]

        ref = case["ref"]
        frame = case["frame"]

        self.info_label.config(
            text=f"Test {self.current_test_index+1}/{len(self.test_cases)} | Ref: {' '.join(map(str, ref))} | Frame: {frame}"
        )

        result = self.engine.run(self.algo_var.get(), ref, frame)
        self.steps = result["results"]
        self.current_step = 0

        self.display_all()

    # ================= DISPLAY =================
    def display_all(self):
        self.tree.delete(*self.tree.get_children())

        for step in self.steps:
            self.tree.insert("", tk.END, values=(
                step["step"],
                step["page"],
                " | ".join(map(str, step["frames"])),
                step["fault"]
            ))

        if self.steps:
            last = self.steps[-1]
            self.draw_frames(last["frames"], last["fault"], last["page"])

        self.result_label.config(
            text=f"Total Faults: {sum(1 for s in self.steps if s['fault'])}"
        )

    def draw_frames(self, frames, is_fault, current):
        for w in self.frame_box.winfo_children():
            w.destroy()

        color = "#ff4d4d" if is_fault else "#2ecc71"

        for p in frames:
            bg = color if p == current else "white"
            tk.Label(self.frame_box, text=str(p), width=5, height=2,
                     bg=bg, relief="solid", font=("Arial", 14, "bold")).pack(side=tk.LEFT, padx=5)

    # ================= STEP =================
    def run_step(self):
        if not self.steps:
            return

        if self.current_step >= len(self.steps):
            return

        step = self.steps[self.current_step]

        self.tree.insert("", tk.END, values=(
            step["step"],
            step["page"],
            " | ".join(map(str, step["frames"])),
            step["fault"]
        ))

        self.draw_frames(step["frames"], step["fault"], step["page"])

        self.current_step += 1

    # ================= AUTO =================
    def toggle_auto(self):
        self.is_auto_playing = not self.is_auto_playing
        self.btn_auto.config(text="STOP" if self.is_auto_playing else "AUTO PLAY")

        if self.is_auto_playing:
            self.auto_run()

    def auto_run(self):
        if self.is_auto_playing and self.current_step < len(self.steps):
            self.run_step()
            self.root.after(700, self.auto_run)
        else:
            self.is_auto_playing = False
            self.btn_auto.config(text="AUTO PLAY")

    # ================= MULTI TEST =================
    def next_test(self):
        if self.current_test_index < len(self.test_cases) - 1:
            self.current_test_index += 1
            self.run_current_test()

    def prev_test(self):
        if self.current_test_index > 0:
            self.current_test_index -= 1
            self.run_current_test()

    # ================= EXTRA =================
    def show_proof(self):
        if not self.test_cases:
            return

        case = self.test_cases[self.current_test_index]
        ref, frame = case["ref"], case["frame"]

        result = {}
        for algo in ["FIFO", "LRU", "OPT"]:
            sim = self.engine.run(algo, ref, frame)
            result[algo] = sum(1 for s in sim["results"] if s["fault"])

        win = tk.Toplevel(self.root)
        win.title("Comparison")

        for algo, val in result.items():
            tk.Label(win, text=f"{algo}: {val} faults").pack()

    def export_csv(self):
        if not self.steps:
            return

        path = filedialog.asksaveasfilename(defaultextension=".csv")
        if path:
            with open(path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Step", "Page", "Frames", "Fault"])
                for s in self.steps:
                    writer.writerow([s["step"], s["page"], s["frames"], s["fault"]])

    def show_help(self):
        messagebox.showinfo("Help", "RUN: chạy\nSTEP: từng bước\nAUTO: tự động\nNEXT/BACK: chuyển test")

    def reset(self):
        self.tree.delete(*self.tree.get_children())
        self.current_step = 0
        self.steps = []
        self.result_label.config(text="Total Faults: 0")


# ================= RUN =================
def main():
    root = tk.Tk()
    app = PageReplacementGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()