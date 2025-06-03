"""
Prova el codi de la classe principal Main.
"""
import unittest
from unittest.mock import patch
from src.main import run

class TestMain(unittest.TestCase):
    """
    Classe de proves per a la classe principal Main.
    """

    def test_should_execute_all_exercises_when_there_is_not_parameters(self):
        """
        Quan no hi ha paràmetres, s'executen tots els exercicis.
        :return:
        """
        with patch('src.modules.exercici1.exercici1.run') as mock_run1, \
             patch('src.modules.exercici2.exercici2.run') as mock_run2, \
             patch('src.modules.exercici3.exercici3.run') as mock_run3, \
             patch('src.modules.exercici4.exercici4.run') as mock_run4, \
             patch('src.modules.exercici5.exercici5.run') as mock_run5:
            run([])
            self.assertTrue(mock_run1.called)
            self.assertTrue(mock_run2.called)
            self.assertTrue(mock_run3.called)
            self.assertTrue(mock_run4.called)
            self.assertTrue(mock_run5.called)

    def test_should_execute_single_exercise_when_send_ex_1(self):
        """
        Quan s'especifica l'exercici 1, només s'executa aquest exercici.
        :return:
        """
        with patch('src.modules.exercici1.exercici1.run') as mock_run1, \
             patch('src.modules.exercici2.exercici2.run') as mock_run2, \
             patch('src.modules.exercici3.exercici3.run') as mock_run3, \
             patch('src.modules.exercici4.exercici4.run') as mock_run4, \
             patch('src.modules.exercici5.exercici5.run') as mock_run5:
            run(['test', '-ex', '1'])
            self.assertTrue(mock_run1.called)
            self.assertFalse(mock_run2.called)
            self.assertFalse(mock_run3.called)
            self.assertFalse(mock_run4.called)
            self.assertFalse(mock_run5.called)

    def test_should_execute_up_to_exercise_when_send_ex_gt_1(self):
        """
        Quan s'especifica un exercici major que 1,
        s'executen també tots els anteriors.
        :return:
        """
        with patch('src.modules.exercici1.exercici1.run') as mock_run1, \
             patch('src.modules.exercici2.exercici2.run') as mock_run2, \
             patch('src.modules.exercici3.exercici3.run') as mock_run3, \
             patch('src.modules.exercici4.exercici4.run') as mock_run4, \
             patch('src.modules.exercici5.exercici5.run') as mock_run5:
            run(['test', '-ex', '3'])
            self.assertTrue(mock_run1.called)
            self.assertTrue(mock_run2.called)
            self.assertTrue(mock_run3.called)
            self.assertFalse(mock_run4.called)
            self.assertFalse(mock_run5.called)

    def test_should_not_execute_any_exercise_when_is_an_invalid_value(self):
        """
        Quan s'especifica un numéro d'exercici incorrecte, emet un error.
        :return:
        """
        with patch('src.modules.exercici1.exercici1.run') as mock_run1, \
             patch('src.modules.exercici2.exercici2.run') as mock_run2, \
             patch('src.modules.exercici3.exercici3.run') as mock_run3, \
             patch('src.modules.exercici4.exercici4.run') as mock_run4, \
             patch('src.modules.exercici5.exercici5.run') as mock_run5:
            run(['test', '-ex', 'fake'])
            self.assertFalse(mock_run1.called)
            self.assertFalse(mock_run2.called)
            self.assertFalse(mock_run3.called)
            self.assertFalse(mock_run4.called)
            self.assertFalse(mock_run5.called)

    def test_should_show_help_when_sending_short_param(self):
        """
        Quan es crida amb el paràmetre -h, es mostra l'ajuda.
        :return:
        """
        with patch('src.modules.help_info.help_info.show_help') as mock_show_help:
            run(['test', '-h'])
            self.assertTrue(mock_show_help.called)

    def test_should_show_help_when_sending_extended_param(self):
        """
        Quan es crida amb el paràmetre --help, es mostra l'ajuda.
        :return:
        """
        with patch('src.modules.help_info.help_info.show_help') as mock_show_help:
            run(['test', '--help'])
            self.assertTrue(mock_show_help.called)

    def test_should_not_execute_any_action_when_the_parameter_is_invalid(self):
        """
        Quan es crida amb el paràmetre --help, es mostra l'ajuda.
        :return:
        """
        with patch('src.modules.exercici1.exercici1.run') as mock_run1, \
                patch('src.modules.exercici2.exercici2.run') as mock_run2, \
                patch('src.modules.exercici3.exercici3.run') as mock_run3, \
                patch('src.modules.exercici4.exercici4.run') as mock_run4, \
                patch('src.modules.exercici5.exercici5.run') as mock_run5, \
                patch('src.modules.help_info.help_info.show_help') as mock_show_help:
            run(['test', 'fake'])
            self.assertFalse(mock_run1.called)
            self.assertFalse(mock_run2.called)
            self.assertFalse(mock_run3.called)
            self.assertFalse(mock_run4.called)
            self.assertFalse(mock_run5.called)
            self.assertFalse(mock_show_help.called)

if __name__ == '__main__':
    unittest.main()
