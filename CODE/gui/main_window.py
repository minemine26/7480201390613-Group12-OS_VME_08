import csv
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
        self.is_auto_playing = False
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
        
        # ===== EXTRA BUTTONS =====
        self.btn_auto = tk.Button(btn_frame, text="AUTO PLAY", bg="purple", fg="white", width=10, command=self.toggle_auto_play)
        self.btn_auto.pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="SHOW PROOF", bg="#e67e22", fg="white", command=self.show_comparison_proof).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="EXPORT", bg="gray", fg="white", command=self.export_gui).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame, text="HELP", bg="#f1c40f", command=self.show_help).pack(side=tk.LEFT, padx=2)

        # ===== VISUALIZATION =====
        self.visual_frame = tk.LabelFrame(self.root, text="Mô phỏng bộ nhớ (Đỏ = Fault, Xanh = Hit)")
        self.visual_frame.pack(fill=tk.X, padx=10, pady=5)
        self.frames_display = tk.Frame(self.visual_frame)
        self.frames_display.pack(pady=10)
        
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
        
        # ===== LOG =====
        tk.Label(self.root, text="Simulation Log:", font=("Arial", 10, "bold")).pack(pady=5)
        self.log_text = tk.Text(self.root, height=6, state=tk.DISABLED, bg="#f9f9f9")
        self.log_text.pack(fill=tk.X, padx=10, pady=5)
        
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
                for item in data:
                    if int(item["frame"]) == frame_count:
                        case = item
                        break
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

    # =========== OVERRIDE LOGIC ===========
    def reset_ui_only(self):
        self.tree.delete(*self.tree.get_children())
        for widget in getattr(self, 'frames_display', tk.Frame()).winfo_children():
            widget.destroy()
        if hasattr(self, 'log_text'):
            self.log_text.config(state=tk.NORMAL)
            self.log_text.delete(1.0, tk.END)
            self.log_text.config(state=tk.DISABLED)

    def reset(self):
        self.reset_ui_only()
        self.result_label.config(text="Total Faults: 0")
        self.info_label.config(text="Reference String:")
        self.current_step = 0
        self.steps = []
        if hasattr(self, 'btn_auto'):
            self.is_auto_playing = False
            self.btn_auto.config(text="AUTO PLAY", bg="purple")

    def display_all(self):
        self.reset_ui_only()
        for step in self.steps:
            self.tree.insert("", tk.END, values=(step["step"], step["page"], " | ".join(map(str, step["frames"])), step["fault"]))
        if self.steps:
            last = self.steps[-1]
            self.draw_frames(last["frames"], last["fault"], last["page"])
            self.write_log({"step": "ALL", "fault": False})
        self.result_label.config(text=f"Total Faults: {sum(1 for s in self.steps if s['fault'])}")

    def run_step(self):
        if not self.steps:
            messagebox.showinfo("Info", "Bấm RUN để nạp dữ liệu trước!")
            return
        if self.current_step == 0:
            self.reset_ui_only()
        if self.current_step >= len(self.steps):
            return

        step = self.steps[self.current_step]
        self.tree.insert("", tk.END, values=(step["step"], step["page"], " | ".join(map(str, step["frames"])), step["fault"]))
        self.draw_frames(step["frames"], step["fault"], step["page"])
        self.write_log(step)

        self.current_step += 1
        self.result_label.config(text=f"Total Faults: {sum(1 for s in self.steps[:self.current_step] if s['fault'])}")
        
        # =========== EXTRA FEATURES ===========
    def draw_frames(self, frames, is_fault, current_page):
        if not hasattr(self, 'frames_display'): return
        for widget in self.frames_display.winfo_children():
            widget.destroy()
        color = "#ff4d4d" if is_fault else "#2ecc71" 
        for p in frames:
            bg_color = color if p == current_page else "white"
            lbl = tk.Label(self.frames_display, text=str(p), width=5, height=2, font=("Arial", 14, "bold"), relief="solid", bg=bg_color)
            lbl.pack(side=tk.LEFT, padx=5)

    def write_log(self, step):
        if not hasattr(self, 'log_text'): return
        self.log_text.config(state=tk.NORMAL)
        if step["step"] == "ALL":
            self.log_text.insert(tk.END, "Hoàn tất mô phỏng toàn bộ.\n")
        else:
            msg = f"Step {step['step']}: Yêu cầu trang {step['page']}.\n"
            msg += f"FAULT (Nạp trang)\n" if step['fault'] else f"HIT (Đã có sẵn)\n"
            msg += "-"*25 + "\n"
            self.log_text.insert(tk.END, msg)
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)

    def toggle_auto_play(self):
        if not self.steps:
            messagebox.showinfo("Info", "Hãy bấm RUN trước để nạp dữ liệu.")
            return
        if self.is_auto_playing:
            self.is_auto_playing = False
            self.btn_auto.config(text="AUTO PLAY", bg="purple")
        else:
            self.is_auto_playing = True
            self.btn_auto.config(text="STOP AUTO", bg="orange")
            if self.current_step >= len(self.steps):
                self.reset_ui_only()
                self.current_step = 0
            self.play_next_step()

    def play_next_step(self):
        if self.is_auto_playing and self.current_step < len(self.steps):
            self.run_step()
            self.root.after(800, self.play_next_step)
        else:
            self.is_auto_playing = False
            self.btn_auto.config(text="AUTO PLAY", bg="purple")

    def show_comparison_proof(self):
        if not self.file_path:
            messagebox.showerror("Lỗi", "Vui lòng chọn file CSV trước!")
            return
        try:
            data = CSVHandler.read_csv(self.file_path)
            if isinstance(data, list) and isinstance(data[0], dict):
                case = data[0]
                frame_input = int(self.frame_entry.get()) if self.frame_entry.get().isdigit() else 3
                for item in data:
                    if int(item["frame"]) == frame_input:
                        case = item
                        break
                ref_list, frame_count = case["ref"], case["frame"]
            else:
                ref_list, data_raw = data, int(self.frame_entry.get())
                frame_count = data_raw

            results = {}
            for algo in ["FIFO", "LRU", "OPT"]:
                sim = self.engine.run(algo, ref_list, frame_count)
                results[algo] = sum(1 for s in sim["results"] if s["fault"])
                
            proof_win = tk.Toplevel(self.root)
            proof_win.title("Proof & Comparison")
            proof_win.geometry("400x300")
            
            tk.Label(proof_win, text="BẢNG SO SÁNH THUẬT TOÁN", font=("Arial", 12, "bold")).pack(pady=10)
            tk.Label(proof_win, text=f"Chuỗi: {ref_list}\nFrame: {frame_count}").pack(pady=5)

            tree = ttk.Treeview(proof_win, columns=("Algo", "Faults"), show="headings", height=4)
            tree.heading("Algo", text="Thuật Toán")
            tree.heading("Faults", text="Total Faults")
            tree.pack(fill=tk.X, padx=20, pady=10)
            
            for algo, faults in results.items():
                tree.insert("", tk.END, values=(algo, faults))
                
            theory_check = results["OPT"] <= results["LRU"] <= results["FIFO"]
            proof_text = "Chuẩn lý thuyết: OPT ≤ LRU ≤ FIFO" if theory_check else "Dữ liệu ngoại lệ (Anomaly)"
            tk.Label(proof_win, text=proof_text, fg="green" if theory_check else "red", font=("Arial", 11, "bold")).pack(pady=5)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_help(self):
        help_text = "1. Choose CSV: Chọn file input.\n2. RUN: Chạy toàn bộ.\n3. STEP / AUTO PLAY: Chạy từng bước trực quan.\n4. SHOW PROOF: Hiện bảng so sánh 3 thuật toán.\n5. EXPORT: Xuất dữ liệu ra file."
        messagebox.showinfo("Hướng Dẫn Sử Dụng", help_text)

    def export_gui(self):
        if not self.steps:
            messagebox.showwarning("Trống", "Chưa có dữ liệu để xuất!")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Step", "Page", "Frames", "Fault"])
                for step in self.steps:
                    writer.writerow([step["step"], step["page"], " | ".join(map(str, step["frames"])), step["fault"]])
            messagebox.showinfo("Thành công", f"Đã lưu kết quả tại:\n{file_path}")

# ================= RUN =================
if __name__ == "__main__":
    root = tk.Tk()
    app = PageReplacementGUI(root)
    root.mainloop()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


def main():
    root = tk.Tk()
    app = PageReplacementGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()