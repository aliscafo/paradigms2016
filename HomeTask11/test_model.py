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


if __name__ == '__main__':
    unittest.main()       
