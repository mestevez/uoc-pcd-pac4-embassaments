"""
Tests pel codi corresponent a l'exercici 5.
"""
import unittest
from io import StringIO
import sys
import pandas as pd
from modules.exercici5 import exercici5

class TestExercise5(unittest.TestCase):
    """
    Classe de test per a l'exercici 5.
    """
    def setUp(self):
        """
        Configuració inicial per a les proves de l'Exercici 5.
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
                799.61, 468.49, 213.67, 213.67, 213.67, 213.67, 213.67, 213.67, 213.67, 213.67, 213.67, 213.67
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
            'nivell_perc_smooth': [
                75.25,  # 2025.10
                59.89,  # 2025.15 *
                57.27,  # 2025.20
                65.38,  # 2025.25 =
                54.24,  # 2025.40 *
                23.85,  # 2025.20
                54.20,  # 2025.70
                75.31,  # 2025.75 =
                57.17,  # 2025.80 *
                59.79,  # 2025.85
                63.17,  # 2025.90 =
                67.31   # 2025.95
            ],
            'volum': [
                62.22, 3.19, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25, 3.25
            ]
        })

    def test_should_print_dry_periods(self):
        """
        Comprova que es mostren els períodes secs correctament.
        """
        captured_output = StringIO()
        sys.stdout = captured_output

        exercici5.run(self.df)

        sys.stdout = sys.__stdout__

        self.assertIn("Períodes de sequera: [", captured_output.getvalue())

    def test_should_calculate_dry_periods(self):
        """
        Comprova que es calculen correctament els períodes secs.
        """
        dry_periods = exercici5.calcula_periodes(self.df)

        self.assertEqual([[2025.15, 2025.25], [2025.40, 2025.75], [2025.80, 2025.90]], dry_periods)


if __name__ == '__main__':
    unittest.main()
