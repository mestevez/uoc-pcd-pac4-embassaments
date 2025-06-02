import sys

def execute_exercise(num: int):
    print (f"Execute {num}")

def execute_exercises(num_from: int, num_to: int):
    for num in range(num_from, num_to + 1):
        execute_exercise(num)

def show_error(err: str):
    print (f"{err}. Use -h or --help for help")

def show_help():
    print ("Show Help")

if __name__ == "__main__":
    if "-h" in sys.argv or "--help" in sys.argv:
        show_help()
    elif len(sys.argv) > 2 and sys.argv[1] == "-ex":
        ex_num = sys.argv[2]
        if ex_num.isnumeric() and 1 <= int(ex_num) <= 5:
            execute_exercises(1, int(ex_num))
        else:
            show_error(f"No such exercise number {ex_num}")
    elif len(sys.argv) <= 1:
        execute_exercises(1, 5)
    else:
        show_error("Unrecognize option")
