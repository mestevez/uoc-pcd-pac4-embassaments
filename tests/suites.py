"""
Definició de les suites de tests
"""
import unittest
from tests.test_exercici1 import TestExercise1
from tests.test_exercici2 import TestExercise2
from tests.test_exercici3 import TestExercise3
from tests.test_exercici4 import TestExercise4
from tests.test_exercici5 import TestExercise5

def suite_exercici1():
    """
    Definició de la suite de tests per a l'exercici 1.
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestExercise1))
    return suite

def suite_exercici2():
    """
    Definició de la suite de tests per a l'exercici 2.
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestExercise2))
    return suite

def suite_exercici3():
    """
    Definició de la suite de tests per a l'exercici 3.
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestExercise3))
    return suite

def suite_exercici4():
    """
    Definició de la suite de tests per a l'exercici 4.
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestExercise4))
    return suite

def suite_exercici5():
    """
    Definició de la suite de tests per a l'exercici 5.
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestExercise5))
    return suite
