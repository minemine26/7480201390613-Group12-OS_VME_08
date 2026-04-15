import sys
import os

# ===== FIX PATH =====
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CODE_DIR = os.path.join(ROOT_DIR, "CODE")

if CODE_DIR not in sys.path:
    sys.path.append(CODE_DIR)


# ===== RUN =====

def run_simulation():
    try:
        from main_logic import main
        print("\n[INFO] Running Simulation...\n")
        main()
    except Exception as e:
        print("[ERROR] Simulation:", e)


def run_gui():
    try:
        from gui.main_window import main
        print("\n[INFO] Opening GUI...\n")
        main()
    except Exception as e:
        print("[ERROR] GUI:", e)


def run_test_algorithms():
    try:
        from test.test_algorithms import main
        print("\n[INFO] Running Test Algorithms...\n")
        main()
    except Exception as e:
        print("[ERROR] Test Algorithms:", e)


def run_test_csv():
    try:
        from test.test_from_csv import main
        print("\n[INFO] Running CSV Test...\n")
        main()
    except Exception as e:
        print("[ERROR] Test CSV:", e)


# ===== MENU =====

def show_menu():
    print("\n==============================")
    print("      OS PROJECT MENU")
    print("==============================")
    print("1. Simulation")
    print("2. GUI")
    print("3. Test Algorithms")
    print("4. Test CSV")
    print("0. Exit")
    print("==============================")


def main():
    while True:
        show_menu()
        choice = input("Chọn: ").strip()

        if choice == "1":
            run_simulation()
        elif choice == "2":
            run_gui()
        elif choice == "3":
            run_test_algorithms()
        elif choice == "4":
            run_test_csv()
        elif choice == "0":
            print("Thoát.")
            break
        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()