"""
Exercici 1. Load dataset i EDA
"""
from pathlib import Path
import pandas

def run() -> pandas.DataFrame:
    """
    Executa l'exercici 1 de la pràctica.
    :return: DataFrame amb el dataset carregat.
    """
    print("======================================")
    print("Executing Exercise 1")
    print("======================================")
    print("1.1 - Carrega el dataset en un dataframe de Pandas:")
    data_path = Path(__file__).parent.parent.parent.parent / "data" / "Quantitat_d_aigua_als_embassaments_de_les_Conques_Internes_de_Catalunya_20250531.csv"
    df: pandas.DataFrame = pandas.read_csv(data_path)
    print("\t... Dataset carregat amb èxit\n")

    print("1.2 - Mostra les 5 primeres files:")
    print(df.head(5))
    print("\n")

    print("1.3 - Mostra les columnes del dataframe:")
    for c in df.columns.tolist():
        print(f"- {c}")
    print("\n")

    print("1.4 - Mostra la informació (info()):")
    print(df.info())
    print("\n")

    return df
