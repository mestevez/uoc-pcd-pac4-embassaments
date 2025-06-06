"""
Tests pel codi corresponent a l'exercici 4.
"""
import unittest
from unittest.mock import patch
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
                pd.Timestamp('2024-03-01 00:00:00'),
                pd.Timestamp('2025-05-29 00:00:00'),
                pd.Timestamp('2025-10-30 00:00:00')
            ],
            'dia_decimal': [
                2024.2,
                2025.4,
                2025.8
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

    def test_should_generate_graphic(self):
        """
        Comprova que es genera correctament la gràfica de l'evolució del volum d'aigua.
        """
        with patch('matplotlib.pyplot.savefig') as mock_pyplot_savefig:
            exercici4.run(self.df)

            mock_pyplot_savefig.assert_called_once_with("screenshots/labaells_smoothed_marc_estevez_amen.png")

if __name__ == '__main__':
    unittest.main()
