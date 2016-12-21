import operator
import unittest
from unittest.mock import patch
from io import *
from model import *
    

class TestNumber(unittest.TestCase):
    def test_number(self):
        abc = Scope()
        abc['a'] = Number(100)                
        with patch("sys.stdout", new_callable=StringIO) as out_number:
            Print(abc["a"]).evaluate(abc)    
            self.assertEqual(out_number.getvalue(), str(100) + '\n')

class TestScope(unittest.TestCase):
    def test_scope(self):
        scope = Scope()
        scope["num"] = Number(505)
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            Print(scope["num"]).evaluate(scope)    
            self.assertEqual(mock_out.getvalue(), str(505) + '\n')

    def test_level(self):
        a = Scope()
        a["foo"] = Number(2)
        b = Scope(a)
        c = Scope(b)
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            Print(c["foo"]).evaluate(c)    
            self.assertEqual(mock_out.getvalue(), str(2) + '\n')
 
#@patch("sys.stdout", new_callable=StringIO)
#def check():
    
class TestBinaryOperation:
    def test_mult(self):
        scope = Scope()
        
        bin_op = BinaryOperation(Number(100), '+', Number(40))
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            Print(bin_op).evaluate(scope)
            self.assertEqual(mock_out.getvalue(), str(140) + '\n')


if __name__ == '__main__':
    unittest.main()       
