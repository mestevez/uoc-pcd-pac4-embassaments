"""
Exercici 4
"""
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import savgol_filter

def smooth_data(df: pd.Series):
    """
    Suavitza les dades d'un DataFrame utilitzant el filtre Savitzky-Golay.
    :param df: Sèrie de dades a suavitzar.
    :return: Sèrie de dades suavitzada.
    """
    window_length = min(1500, len(df))
    polyorder = min(3, window_length - 1)
    return savgol_filter(df, window_length=window_length, polyorder=polyorder)

def print_graph(df: pd.DataFrame, graph_destination: str):
    """
    Imprimeix una representació gràfica de l'evolució del volum d'aigua amb el gràfic suavitzat.
    :param df: DataFrame amb les dades a representar.
    """
    plt.figure(figsize=(7, 5))
    plt.plot(df['dia_decimal'], df['nivell_perc'])
    plt.plot(
        df['dia_decimal'],
        df['nivell_perc_smooth'],
        marker=0,
        color='orange',
        label='smoothed',
        linewidth=5
    )
    plt.suptitle('Embassament de La Baells')
    plt.title('Marc Estévez Amén')
    plt.xlabel('temps')
    plt.ylabel('percentatge (%)')
    plt.legend(loc='lower center')
    plt.savefig(graph_destination)

def run(df: pd.DataFrame) -> pd.DataFrame:
    """
    Executa l'exercici 4 de la pràctica.
    :param df: DataFrame a utilitzar per a l'exercici.
    :return: None
    """
    print("======================================")
    print("Executing Exercise 4")
    print("======================================")
    dfu = df.copy()

    print("4.1 - Crea la columna nivell_perc_smooth amb les dades suavitzades:")
    dfu.insert(5, 'nivell_perc_smooth', smooth_data(dfu['nivell_perc']))
    print("\t... Columna nivell_perc_smooth creada amb èxit\n")

    print("4.2 - Representeu gràficament el senyal original amb el senyal suavitzat:")
    graph_destination = "screenshots/labaells_smoothed_marc_estevez_amen.png"
    print_graph(dfu, graph_destination)
    print(f"\t... Gràfica generada i guardada a: {graph_destination}\n")

    return dfu

