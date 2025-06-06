"""
Fitxer d'entrada per a la pràctica de Python.
Proporciona una gestió bàsica dels paràmetres d'entrada per executar exercicis,
o ofereix funcionalitats bàsiques com l'ajuda.
"""
import sys
import pandas
from modules.exercici1 import exercici1
from modules.exercici2 import exercici2
from modules.exercici3 import exercici3
from modules.exercici4 import exercici4
from modules.exercici5 import exercici5
from modules.help_info import help_info

def verify_dataframe(df: None | pandas.DataFrame) -> pandas.DataFrame:
    """
    Verifica si el DataFrame està definit. Si no ho és, llança un error.
    :param df: DataFrame a verificar.
    :return: El DataFrame si és vàlid.
    """
    if df is None:
        raise ValueError("DataFrame is not valid. Please run Exercise 1 first.")

    return df

def execute_exercise(num: int, df: None | pandas.DataFrame) -> None | pandas.DataFrame:
    """
    Executa un exercici de la pràctica de forma individual.
    :param num: Número de l'exercici a executar.
    :param df: DataFrame a utilitzar per als exercicis que ho requereixin.
    :return:
    """

    if num == 1:
        df = exercici1.run()
    elif num == 2:
        df = exercici2.run(verify_dataframe(df))
    elif num == 3:
        df = exercici3.run(verify_dataframe(df))
    elif num == 4:
        exercici4.run()
    elif num == 5:
        exercici5.run()

    return df


def execute_exercises(num_from: int, num_to: int):
    """
    Executa els exercicis de la pràctica dins d'un rang determinat.
    :param num_from: Número d'inici del rang d'exercicis.
    :param num_to: Número final del rang d'exercicis.
    :return:
    """
    df: None | pandas.DataFrame = None

    for num in range(num_from, num_to + 1):
        df = execute_exercise(num, df)

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
