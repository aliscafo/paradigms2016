from operator import (add, floordiv, mod, sub, mul, lt, le, not_, gt, ge, ne, eq, neg)
import unittest
from unittest.mock import patch
from io import *
from model import *
    

class TestNumber(unittest.TestCase):
    def test_number(self):
        abc = Scope()
        abc['a'] = Number(100)                
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            Print(abc["a"]).evaluate(abc)    
            self.assertEqual(mock_out.getvalue(), str(100) + '\n')

@patch("sys.stdout", new_callable=StringIO)
def check(obj, res, mock_out):
    scope = Scope()
    Print(obj.evaluate(scope)).evaluate(scope)
    return (mock_out.getvalue() == (str(res) + '\n')) 
    

class TestFunction(unittest.TestCase):
    def test_inst(self):
        assert check((Function(('hello', 'world'), [Number(5), Number(7)])), 7)       
          

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
     
     
class TestBinaryOperation(unittest.TestCase):
    def test_eval(self):    
        
        operations = {"+" : add,
                  "-" : sub,
                  "*" : mul,   
                  "/" : floordiv,
                  "%" : mod,
                  "==" : eq,
                  "!=" : ne,
                  "<" : lt,
                  ">" : gt,
                  "<=" : le,
                  ">=" : ge,
                  "&&" : lambda x, y: bool(x and y),  
                  "||" : lambda x, y: bool(x or y)}
        
        
        for a in range(-2, 2):
            for b in range(-2, 2):
                for op, f in operations.items():
                    if b != 0 or (op != '/' and op != '%'):
                        assert check(BinaryOperation(Number(a), op, Number(b)), f(a,b))


class TestUnaryOperation(unittest.TestCase):
    def test_eval(self):    
        operations = {"!" : not_,
                      "-" : neg}
    
        for a in range(-2, 2):
            for op, f in operations.items():
                assert check(UnaryOperation(op, Number(a)), f(a))
        

if __name__ == '__main__':
    unittest.main()       
