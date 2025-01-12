import unittest
import sys
sys.path.append("..")  # Adds the parent directory to the sys.path
from translator import *

# Now you can use your_module functions and classes

class TestEnToFr(unittest.TestCase):
    def test1(self): 
        self.assertIsNone(englishToFrench(""))
        self.assertEqual(englishToFrench("Hello"),"Bonjour" )

class TestFrToEn(unittest.TestCase):
    def test1(self): 
        self.assertIsNone(frenchToEnglish(""))
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello" )
        
unittest.main()
