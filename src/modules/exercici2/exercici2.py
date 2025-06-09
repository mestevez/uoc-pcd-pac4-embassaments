"""
Exercici 2: neteja de les dades i filtratge
"""
import re
import pandas

def reformat_swamp_name(name: str) -> str:
    """
    Reanomena els embassaments de manera que 'Embassament de Darnius Boadella (Darnius)'
    passa a dir-se 'Darnius Boadella'.
    És a dir, suprimeix 'Embassament de ' i suprimeix el municipi que està entre parèntesi.
    :param name: Nom original de l'embassament.
    :return: Nom reformatat de l'embassament.
    """
    renamed: str = re.sub(r"^Embassament\sde\s+([^(]+)\s*(?:\([^)]+\))?\s*$", r"\1", name).strip()

    return renamed[0].upper() + renamed[1:]  # Capitalitza la primera lletra

def run(df: pandas.DataFrame) -> pandas.DataFrame:
    """
    Executa l'exercici 2 de la pràctica.
    :param df: DataFrame a utilitzar per a l'exercici.
    :return: DataFrame amb les operacions realitzades.
    """
    print("======================================")
    print("Executing Exercise 2")
    print("======================================")

    print("2.1 - Reanomenar columnes:")
    udf = df.rename(copy=True, columns={
        "Dia": "dia",
        "Estació":"estacio",
        "Nivell absolut (msnm)":"nivell_msnm",
        "Percentatge volum embassat (%)": "nivell_perc",
        "Volum embassat (hm3)": "volum"
    })
    print(f"\t... Columnes reanomenades amb èxit: {udf.columns.tolist()}\n")

    print("2.2 - Mostra els valors únics del nom dels embassaments:")
    print(udf['estacio'].unique())
    print("\n")

    print("2.3 - Reanomena els embassaments:")
    for swamp_index in range(len(udf)):
        udf.at[swamp_index, 'estacio'] = reformat_swamp_name(udf['estacio'].iloc[swamp_index])
    print(f"\t... Embassaments reanomenats amb èxit: {udf['estacio'].unique()}\n")

    print("2.4 - Crea un nou dataframe filtrant per La Baells:")
    udf = udf[udf['estacio'] == "La Baells"]
    print(f"\t... Dataframe filtrat amb èxit: len={len(udf)}\n")

    return udf
