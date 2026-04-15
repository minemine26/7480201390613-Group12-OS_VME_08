import sys
import os

# ================== FIX PATH ==================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)


# ================== RUN FUNCTIONS ==================

def run_simulation():
    """Chạy mô phỏng chính"""
    try:
        from main_logic import main as simulation_main
        print("\n[INFO] Running Simulation...\n")
        simulation_main()
    except Exception as e:
        print("[ERROR] Simulation:", e)


def run_gui():
    """Chạy GUI"""
    try:
        print("\n[INFO] Opening GUI...\n")
        from gui.main_window import main as gui_main
        gui_main()
    except Exception as e:
        print("[ERROR] GUI:", e)


def run_test_algorithms():
    """Chạy test thuật toán"""
    try:
        print("\n[INFO] Running Algorithm Tests...\n")
        from test.test_algorithms import main as test_algo_main
        test_algo_main()
    except Exception as e:
        print("[ERROR] Test Algorithms:", e)


def run_test_csv():
    """Chạy test CSV và export full multi-test"""
    try:
        print("\n[INFO] Running CSV Test (Multi-case + Comparison)...\n")

        import importlib
        test_module = importlib.import_module("test.test_from_csv")
        importlib.reload(test_module)
        test_module.main()

    except ModuleNotFoundError as e:
        print("[ERROR] Không tìm thấy module test:", e)

    except AttributeError:
        print("[ERROR] File test_from_csv.py không có hàm main()")

    except Exception as e:
        print("[ERROR] Test CSV:", e)


# ================== MENU ==================

def show_menu():
    print("\n==============================")
    print("      OS PROJECT MENU")
    print("==============================")
    print("1. Chạy mô phỏng (Simulation)")
    print("2. Chạy GUI")
    print("3. Test thuật toán")
    print("4. Test CSV (xuất output)")
    print("0. Thoát")
    print("==============================")


def handle_choice(choice):
    if choice == "1":
        run_simulation()
    elif choice == "2":
        run_gui()
    elif choice == "3":
        run_test_algorithms()
    elif choice == "4":
        run_test_csv()
    elif choice == "0":
        print("Thoát chương trình.")
        sys.exit(0)
    else:
        print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")


# ================== MAIN ==================

def main():
    """Entry point của hệ thống"""
    while True:
        try:
            show_menu()
            choice = input("Chọn chức năng: ").strip()
            handle_choice(choice)
        except KeyboardInterrupt:
            print("\n[INFO] Dừng chương trình.")
            sys.exit(0)
        except Exception as e:
            print("[ERROR] Unexpected:", e)


if __name__ == "__main__":
    main()