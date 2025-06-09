"""
Tests pel codi corresponent a l'exercici 3.
"""
import unittest
from unittest.mock import patch
from pathlib import Path
from io import StringIO
import sys
import pandas as pd
from modules.exercici3 import exercici3

class TestExercise3(unittest.TestCase):
    """
    Classe de test per a l'exercici 3.
    """

    def setUp(self):
        """
        Configuració inicial per a les proves de l'Exercici 3.
        Genera un DataFrame amb dades d'exemple i l'estructura esperada en aquest punt de la pràctica.
        """
        self.df = pd.DataFrame({
            'dia': [
                '30/10/2025',
                '29/05/2025',
                '01/03/2024',
            ],
            'estacio': [
                'La Baells',
                'La Baells',
                'La Baells',
            ],
            'nivell_msnm': [
                799.61, 468.49, 213.67
            ],
            'nivell_perc': [
                77.8, 26.1, 61.2
            ],
            'volum': [
                62.22, 3.19, 3.25
            ]
        })

    def test_should_run_exercise_and_return_updated_dataframe(self):
        """
        Executa l'exercici 3 i comprova que retorna un DataFrame actualitzat.
        """
        dfu = exercici3.run(self.df)

        self.assertIsNotNone(dfu)

    def test_should_convert_dia_into_datetime(self):
        """
        Comprova que la columna 'dia' s'ha convertit correctament a datetime.
        """
        dfu = exercici3.run(self.df)

        self.assertEqual(type (dfu['dia'].iloc[0]), pd.Timestamp)
        self.assertEqual(dfu['dia'].iloc[0], pd.Timestamp('2024-03-01 00:00:00'))
        self.assertEqual(dfu['dia'].iloc[1], pd.Timestamp('2025-05-29 00:00:00'))
        self.assertEqual(dfu['dia'].iloc[2], pd.Timestamp('2025-10-30 00:00:00'))


    def test_should_sort_dataframe_by_date_ascendant(self):
        """
        Comprova que el DataFrame s'ha ordenat per la columna 'dia' de manera ascendent.
        """
        dfu = exercici3.run(self.df)

        self.assertEqual(dfu['dia'].iloc[0], pd.Timestamp('2024-03-01'))
        self.assertEqual(dfu['dia'].iloc[2], pd.Timestamp('2025-10-30'))


    def test_should_show_min_and_max_dates(self):
        """
        Comprova que s'indiquen les dates mínima i màxima del DataFrame.
        """
        captured_output = StringIO()
        sys.stdout = captured_output

        exercici3.run(self.df)

        sys.stdout = sys.__stdout__
        self.assertIn("Data més antiga: 2024-03-01 00:00:00", captured_output.getvalue())
        self.assertIn("Data més nova: 2025-10-30 00:00:00", captured_output.getvalue())


    def test_should_create_dia_decimal_column(self):
        """
        Comprova que el DataFrame s'ha ordenat per la columna 'dia' de manera ascendent.
        """
        dfu = exercici3.run(self.df)

        self.assertIn('dia_decimal', dfu.columns)
        self.assertAlmostEqual(dfu['dia_decimal'].iloc[0], 2024.2, places=1)
        self.assertAlmostEqual(dfu['dia_decimal'].iloc[1], 2025.4, places=1)
        self.assertAlmostEqual(dfu['dia_decimal'].iloc[2], 2025.8, places=1)


    def test_should_convert_date_to_year_fraction(self):
        """
        Comprova que la funció to_year_to_fraction converteix correctament les dates a un valor decimal de l'any.
        """
        date = pd.Timestamp('2025-06-15')

        result = exercici3.to_year_to_fraction(date)

        self.assertAlmostEqual(result, 2025.5, places=1)


    def test_should_generate_graphic(self):
        """
        Comprova que es genera correctament la gràfica de l'evolució del volum d'aigua.
        """
        with patch('matplotlib.pyplot.savefig') as mock_pyplot_savefig:
            exercici3.run(self.df)

            graph_path = Path(__file__).parent.parent / "screenshots" / "labaells_marc_estevez_amen.png"
            mock_pyplot_savefig.assert_called_once_with(graph_path)


if __name__ == '__main__':
    unittest.main()
