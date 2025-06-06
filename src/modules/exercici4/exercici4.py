"""
Exercici 4
"""
import matplotlib.pyplot as plt
import pandas
from scipy.signal import savgol_filter

def smoth_data(df: pandas.Series):
    """
    Suavitza les dades d'un DataFrame utilitzant el filtre Savitzky-Golay.
    :param df: Sèrie de dades a suavitzar.
    :return: Sèrie de dades suavitzada.
    """
    window_length = min(1500, len(df))
    polyorder = min(3, window_length - 1)
    return savgol_filter(df, window_length=window_length, polyorder=polyorder)

def print_graph(df: pandas.DataFrame):
    """
    Imprimeix una representació gràfica de l'evolució del volum d'aigua amb el gràfic suavitzat.
    :param df: DataFrame amb les dades a representar.
    """
    plt.figure(figsize=(7, 5))
    plt.plot(df['dia_decimal'], df['nivell_perc'])
    plt.plot(
        df['dia_decimal'],
        smoth_data(df['nivell_perc']),
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
    plt.savefig("screenshots/labaells_smoothed_marc_estevez_amen.png")

def run(df: pandas.DataFrame):
    """
    Executa l'exercici 4 de la pràctica.
    :param df: DataFrame a utilitzar per a l'exercici.
    :return: None
    """
    print("======================================")
    print("Executing Exercise 4")
    print("======================================")

    print("4.1 - Representeu gràficament el senyal original amb el senyal suavitzat :")
    print_graph(df)
    print("\t... Gràfica generada amb èxit\n")

