"""
Tests pel codi corresponent a l'exercici 4.
"""
import unittest
from unittest.mock import patch
from pathlib import Path
import pandas as pd
from modules.exercici4 import exercici4


class TestExercise4(unittest.TestCase):
    """
    Classe de test per a l'exercici 4.
    """

    def setUp(self):
        """
        Configuració inicial per a les proves de l'Exercici 4.
        Genera un DataFrame amb dades d'exemple i l'estructura esperada en aquest punt de la pràctica.
        """
        self.df = pd.DataFrame({
            'dia': [
                pd.Timestamp('2025-01-01 00:00:00'),
                pd.Timestamp('2025-02-01 00:00:00'),
                pd.Timestamp('2025-03-01 00:00:00'),
                pd.Timestamp('2025-04-01 00:00:00'),
                pd.Timestamp('2025-05-01 00:00:00'),
                pd.Timestamp('2025-06-01 00:00:00'),
                pd.Timestamp('2025-07-01 00:00:00'),
                pd.Timestamp('2025-08-01 00:00:00'),
                pd.Timestamp('2025-09-01 00:00:00'),
                pd.Timestamp('2025-10-01 00:00:00'),
                pd.Timestamp('2025-11-01 00:00:00'),
                pd.Timestamp('2025-12-01 00:00:00')
            ],
            'dia_decimal': [
                2025.10,
                2025.15,
                2025.20,
                2025.25,
                2025.40,
                2025.20,
                2025.70,
                2025.75,
                2025.80,
                2025.85,
                2025.90,
                2025.95
            ],
            'estacio': [
                'La Baells',
                'La Baells',
                'La Baells',
                'La Baells',
                'La Baells',
                'La Baells',
                'La Baells',
                'La Baells',
                'La Baells',
                'La Baells',
                'La Baells',
                'La Baells'
            ],
            'nivell_msnm': [
                799.61, 468.49, 213.67, 213.67, 213.67,
                213.67, 213.67, 213.67, 213.67, 213.67, 213.67, 213.67
            ],
            'nivell_perc': [
                77.8,
                26.1,
                61.2,
                80.2,
                73.2,
                25.2,
                30.2,
                72.2,
                76.2,
                58.2,
                45.2,
                75.2
            ],
            'volum': [
                62.22, 3.19, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25
            ]
        })

    def test_should_run_exercise_and_return_updated_dataframe(self):
        """
        Executa l'exercici 4 i comprova que retorna un DataFrame actualitzat.
        """
        dfu = exercici4.run(self.df)

        self.assertIsNotNone(dfu)


    def test_should_create_column_with_smooth_data(self):
        """
        Comprova que s'ha creat correctament la columna amb les dades suavitzades.
        """
        dfu = exercici4.run(self.df)

        self.assertIn('nivell_perc_smooth', dfu.columns)
        self.assertAlmostEqual(63.25, dfu['nivell_perc_smooth'].iloc[0], places=1)
        self.assertAlmostEqual(59.89, dfu['nivell_perc_smooth'].iloc[1], places=1)
        self.assertAlmostEqual(57.27, dfu['nivell_perc_smooth'].iloc[2], places=1)
        self.assertAlmostEqual(55.38, dfu['nivell_perc_smooth'].iloc[3], places=1)
        self.assertAlmostEqual(54.24, dfu['nivell_perc_smooth'].iloc[4], places=1)
        self.assertAlmostEqual(53.85, dfu['nivell_perc_smooth'].iloc[5], places=1)
        self.assertAlmostEqual(54.20, dfu['nivell_perc_smooth'].iloc[6], places=1)
        self.assertAlmostEqual(55.31, dfu['nivell_perc_smooth'].iloc[7], places=1)
        self.assertAlmostEqual(57.17, dfu['nivell_perc_smooth'].iloc[8], places=1)
        self.assertAlmostEqual(59.79, dfu['nivell_perc_smooth'].iloc[9], places=1)
        self.assertAlmostEqual(63.17, dfu['nivell_perc_smooth'].iloc[10], places=1)
        self.assertAlmostEqual(67.31, dfu['nivell_perc_smooth'].iloc[11], places=1)


    def test_should_generate_graphic(self):
        """
        Comprova que es genera correctament la gràfica de l'evolució del volum d'aigua.
        """
        with patch('matplotlib.pyplot.savefig') as mock_pyplot_savefig:
            exercici4.run(self.df)

            graph_path = Path(__file__).parent.parent / "screenshots" / "labaells_smoothed_marc_estevez_amen.png"
            mock_pyplot_savefig.assert_called_once_with(graph_path)

if __name__ == '__main__':
    unittest.main()
