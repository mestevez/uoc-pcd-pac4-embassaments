"""
Exercici 3
"""
from datetime import datetime as dt
import time
from pathlib import Path
import matplotlib.pyplot as plt
import pandas

def since_epoch(date: pandas.Timestamp | dt) -> float:
    """
    Converteix una data a un valor de temps en segons des de l'època (1 de gener de 1970).
    :param date: Data a convertir.
    :return: Valor de temps en segons des de l'època.
    """
    return time.mktime(date.timetuple())

def to_year_to_fraction(date: pandas.Timestamp) -> float:
    """
    Converteix una data a un valor decimal que representa l'any.
    Per exemple, 01/07/2025 hauria de ser aproximadament 2025.5.
    :param date: Data a convertir.
    :return: Valor decimal de l'any.
    """

    year = date.year
    start_of_this_year = dt(year=year, month=1, day=1)
    start_of_next_year = dt(year=year+1, month=1, day=1)

    year_elapsed = since_epoch(date) - since_epoch(start_of_this_year)
    year_duration = since_epoch(start_of_next_year) - since_epoch(start_of_this_year)
    fraction = year_elapsed/year_duration

    return date.year + fraction

def print_graph(df: pandas.DataFrame, graph_path: Path):
    """
    Imprimeix una representació gràfica de l'evolució del volum d'aigua.
    :param df: DataFrame amb les dades a representar.
    :param graph_path: Ruta on es guardarà la gràfica.
    """
    plt.figure(figsize=(7, 5))
    plt.plot(df['dia_decimal'], df['nivell_perc'])
    plt.suptitle('Embassament de La Baells')
    plt.title('Marc Estévez Amén')
    plt.xlabel('temps')
    plt.ylabel('percentatge (%)')
    plt.savefig(graph_path)


def run(df: pandas.DataFrame) -> pandas.DataFrame:
    """
    Executa l'exercici 3 de la pràctica.
    :param df: DataFrame a utilitzar per a l'exercici.
    :return: DataFrame amb les operacions realitzades.
    """
    print("======================================")
    print("Executing Exercise 3")
    print("======================================")
    dfu = df.copy()

    print("3.1 - Convertir a datetime:")
    dfu['dia'] = pandas.to_datetime(dfu['dia'], format='%d/%m/%Y')
    print("\t... Columna dia convertida a datetime amb èxit\n")

    print("3.2 - Quantes dades tenim?")
    dfu.sort_values(by='dia', ascending=True, inplace=True)
    print("\t... Dataframe ordenat per dia ASC\n")
    print(f"Data més antiga: {dfu['dia'].min()}")
    print(f"Data més nova: {dfu['dia'].max()}\n")

    print("3.3 - Crea la columna dia_decimal (en una linea):")
    dfu.insert(1, 'dia_decimal', dfu['dia'].apply(to_year_to_fraction))
    print("\t... Columna dia_decimal creada amb èxit\n")

    print("3.4 - Representació gràfica de l'evolució del volum d'aigua:")
    graph_path = Path(__file__).parent.parent.parent.parent / "screenshots" / "labaells_marc_estevez_amen.png"
    print_graph(dfu, graph_path)
    print(f"\t... Gràfica generada i guardada a: {graph_path}\n")

    return dfu
