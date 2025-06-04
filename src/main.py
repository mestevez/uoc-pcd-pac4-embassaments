"""
Fitxer d'entrada per a la pràctica de Python.
Proporciona una gestió bàsica dels paràmetres d'entrada per executar exercicis,
o ofereix funcionalitats bàsiques com l'ajuda.
"""
import sys
from modules.exercici1 import exercici1
from modules.exercici2 import exercici2
from modules.exercici3 import exercici3
from modules.exercici4 import exercici4
from modules.exercici5 import exercici5
from modules.help_info import help_info

def execute_exercise(num: int):
    """
    Executa un exercici de la pràctica de forma individual.
    :param num: Número de l'exercici a executar.
    :return:
    """

    if num == 1:
        exercici1.run()
    elif num == 2:
        exercici2.run()
    elif num == 3:
        exercici3.run()
    elif num == 4:
        exercici4.run()
    elif num == 5:
        exercici5.run()


def execute_exercises(num_from: int, num_to: int):
    """
    Executa els exercicis de la pràctica dins d'un rang determinat.
    :param num_from: Número d'inici del rang d'exercicis.
    :param num_to: Número final del rang d'exercicis.
    :return:
    """
    for num in range(num_from, num_to + 1):
        execute_exercise(num)

def show_error(err: str):
    """
    Mostra un missatge d'error en els paràmetres d'entrada. Hi afegeix un missatge d'ajuda.
    :param err: Missatge d'error a mostrar.
    :return:
    """
    print (f"{err}. Use -h or --help for help")

def run(argv: list[str]) -> None:
    """
    Gestiona els paràmetres d'entrada i executa les funcions corresponents.
    :param argv: Llista de paràmetres d'entrada.
    :return:
    """
    if "-h" in argv or "--help" in argv:
        help_info.show_help()
    elif len(argv) > 2 and argv[1] == "-ex":
        ex_num = argv[2]
        if ex_num.isnumeric() and 1 <= int(ex_num) <= 5:
            execute_exercises(1, int(ex_num))
        else:
            show_error(f"No such exercise number {ex_num}")
    elif len(argv) <= 1:
        execute_exercises(1, 5)
    else:
        show_error("Unrecognize option")

if __name__ == "__main__":
    run(sys.argv)
