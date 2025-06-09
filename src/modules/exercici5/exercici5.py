"""
Exercici 5:
"""
import pandas as pd

def calcula_periodes(df: pd.DataFrame)-> list[list[float]]:
    """
    Calcula els períodes de sequera en un DataFrame.
    Es defineix període de sequera com un interval de temps on el percentatge suavitzat de l'aigua és inferior al 60%.
    :param df: DataFrame amb les dades a analitzar.
    :return: DataFrame amb els períodes de sequera data_index inundació.
    """
    threshold = 60

    dry_periods = []
    current_period = []

    for _index, row in df.iterrows():
        if row['nivell_perc_smooth'] < threshold:
            if not current_period:
                current_period.append(row['dia_decimal'])
        else:
            if current_period:
                current_period.append(row['dia_decimal'])
                dry_periods.append(current_period)
                current_period = []

    return dry_periods


def run(df: pd.DataFrame):
    """
    Executa l'exercici 5 de la pràctica.
    :param df: DataFrame a utilitzar per a l'exercici.
    :return: None
    """
    print("======================================")
    print("Executing Exercise 5")
    print("======================================")

    print("5.1 - Calcula els períodes de sequera:")
    dry_periods = calcula_periodes(df)
    print(f"Períodes de sequera: {dry_periods}\n")
