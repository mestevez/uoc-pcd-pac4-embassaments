"""
Tests pel codi corresponent a l'exercici 1.
"""
import unittest
import sys
from io import StringIO
from modules.exercici1 import exercici1


class TestExercise1(unittest.TestCase):
    """
    Classe de test per a l'exercici 1.
    """

    def test_should_run_exercise_and_return_dataframe(self):
        """
        Executa l'exercici 1 i comprova que retorna un DataFrame.
        """
        df = exercici1.run()

        self.assertIsNotNone(df)

    def test_should_run_exercise_and_show_first_rows(self):
        """
        Executa l'exercici 1 i comprova que es mostren les primeres files del DataFrame.
        """
        captured_output = StringIO()
        sys.stdout = captured_output

        exercici1.run()

        sys.stdout = sys.__stdout__
        self.assertIn("0  30/05/2025", captured_output.getvalue())
        self.assertIn("1  30/05/2025", captured_output.getvalue())
        self.assertIn("2  30/05/2025", captured_output.getvalue())
        self.assertIn("3  30/05/2025", captured_output.getvalue())
        self.assertIn("4  30/05/2025", captured_output.getvalue())

    def test_should_run_exercise_and_show_all_columns(self):
        """
        Executa l'exercici 1 i comprova que es mostren totes les columnes del DataFrame.
        """
        captured_output = StringIO()
        sys.stdout = captured_output

        exercici1.run()

        sys.stdout = sys.__stdout__
        self.assertIn("- Dia", captured_output.getvalue())
        self.assertIn("- Estació", captured_output.getvalue())
        self.assertIn("- Nivell absolut (msnm)", captured_output.getvalue())
        self.assertIn("- Percentatge volum embassat (%)", captured_output.getvalue())
        self.assertIn("- Volum embassat (hm3)", captured_output.getvalue())

    def test_should_run_exercise_and_show_info(self):
        """
        Executa l'exercici 1 i comprova que es mostra la informació del DataFrame.
        """
        captured_output = StringIO()
        sys.stdout = captured_output

        exercici1.run()

        sys.stdout = sys.__stdout__
        self.assertIn("RangeIndex: 83538 entries, 0 to 83537", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()
