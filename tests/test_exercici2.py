"""
Tests pel codi corresponent a l'exercici 2.
"""
import unittest
from io import StringIO
import sys
import pandas as pd
from modules.exercici2 import exercici2

class TestExercise2(unittest.TestCase):
    """
    Classe de test per a l'exercici 2.
    """

    def setUp(self):
        """
        Configuració inicial per a les proves de l'Exercici 2.
        """
        self.df = pd.DataFrame({
            'Dia': [
                '30/05/2025', '30/05/2025', '30/05/2025',
                '29/05/2025', '29/05/2025', '29/05/2025',
                '28/05/2025', '28/05/2025', '28/05/2025'
            ],
            'Estació': [
                'Embassament de la Llosa del Cavall (Nav√®s)',
                'Embassament de Darnius Boadella (Darnius)',
                'Embassament de la Baells (Cercs)',
                'Embassament de la Llosa del Cavall (Nav√®s)',
                'Embassament de Darnius Boadella (Darnius)',
                'Embassament de la Baells (Cercs)',
                'Embassament de la Llosa del Cavall (Nav√®s)',
                'Embassament de Darnius Boadella (Darnius)',
                'Embassament de la Baells (Cercs)',
            ],
            'Nivell absolut (msnm)': [
                799.61, 468.49, 213.67, 100.19, 528.44, 347.04, 413.07, 629.09, 154.23
            ],
            'Percentatge volum embassat (%)': [
                77.8, 26.1, 61.2, 94.7, 91, 89.6, 63.5, 97, 76.2
            ],
            'Volum embassat (hm3)': [
                62.22, 3.19, 3.25, 3.54, 22.19, 208.85, 105, 106.15, 46.53
            ]
        })

    def test_should_run_exercise_and_return_updated_dataframe(self):
        """
        Executa l'exercici 2 i comprova que retorna un DataFrame actualitzat.
        """
        dfu = exercici2.run(self.df)

        self.assertIsNotNone(dfu)

    def test_should_run_exercise_and_rename_columns(self):
        """
        Executa l'exercici 2 i comprova que les columnes s'han reanomenat correctament.
        """
        dfu = exercici2.run(self.df)

        self.assertEqual("dia", dfu.columns[0])
        self.assertEqual("estacio", dfu.columns[1])
        self.assertEqual("nivell_msnm", dfu.columns[2])
        self.assertEqual("nivell_perc", dfu.columns[3])
        self.assertEqual("volum", dfu.columns[4])

    def test_should_run_exercise_and_show_unique_swamps(self):
        """
        Executa l'exercici 2 i comprova que es mostren els valors únics dels embassaments.
        """
        captured_output = StringIO()
        sys.stdout = captured_output

        exercici2.run(self.df)

        sys.stdout = sys.__stdout__
        self.assertIn(
            "['Embassament de la Llosa del Cavall (Nav√®s)'\n" +
            " 'Embassament de Darnius Boadella (Darnius)'\n" +
            " 'Embassament de la Baells (Cercs)']",
            captured_output.getvalue()
        )

    def test_should_rename_swamps(self):
        """
        Executa l'exercici 2 i comprova que es reanomenen correctament els embassaments.
        """
        result = exercici2.reformat_swamp_name("Embassament de la Baells (Cercs)")

        self.assertEqual("La Baells", result)

    def test_should_run_exercise_and_filter_by_swamp(self):
        """
        Executa l'exercici 2 i comprova que es filtra correctament per l'embassament La Baells.
        """
        dfu = exercici2.run(self.df)

        self.assertEqual(3, len(dfu))
        self.assertEqual("La Baells", dfu['estacio'].iloc[0])
        self.assertEqual("La Baells", dfu['estacio'].iloc[1])
        self.assertEqual("La Baells", dfu['estacio'].iloc[2])

if __name__ == '__main__':
    unittest.main()
