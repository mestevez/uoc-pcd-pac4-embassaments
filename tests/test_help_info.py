"""
Tests pel codi corresponent al mòdul d'ajuda.
"""
import unittest
from io import StringIO
import sys
from modules.help_info import help_info

class TestHelpInfo(unittest.TestCase):
    """
    Classe de test per mostrar l'ajuda
    """

    def test_should_print_help(self):
        """
        Comprova que s'imprimeix la informació d'ajuda quan s'executa el mòdul d'ajuda.
        :return:
        """
        captured_output = StringIO()
        sys.stdout = captured_output

        help_info.show_help()

        sys.stdout = sys.__stdout__

        self.assertIn("usage: main.py", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()
