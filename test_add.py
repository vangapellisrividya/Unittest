import unittest
import Calculator 

class TestCaseAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.sum(self,50,50),100)

    def test_sub(self):
        self.assertEqual(Calculator.sub(self,30,20),600)

    def test_mul(self):
        self.assertEqual(Calculator.mul(self,30,20),10)

    def test_values(self):
        self.assertRaises(ValueError, Calculator.sum,self, 'jp',10)
        self.assertRaises(ValueError,Calculator.sum,self,"hello","world")

    
        