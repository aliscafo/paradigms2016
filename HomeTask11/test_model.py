from operator import (add, floordiv, mod, sub, mul, lt, le, not_, gt, ge, ne, eq, neg)
import unittest
from unittest.mock import patch
from io import StringIO
from model import *
    

class TestNumber(unittest.TestCase):
    def test_number(self):
        abc = Scope()
        abc['a'] = Number(100)                
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            Print(abc["a"]).evaluate(abc)    
            self.assertEqual(mock_out.getvalue(), str(100) + '\n')
            
            
class TestReference(unittest.TestCase):
    def test_ref(self):
        abc = Scope()
        abc["a"] = Reference("sea")
        abc["sea"] = Number(4)                
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            Print(abc["a"]).evaluate(abc)   
            self.assertEqual(mock_out.getvalue(), str(4) + '\n')

class TestRead(unittest.TestCase):
    def test_read(self):
        scope = Scope()
        with patch("sys.stdin", new=StringIO("1984\n")), patch("sys.stdout", new_callable=StringIO) as mock_out:
            num = Read("Num").evaluate(scope)            
            Print(num).evaluate(scope)    
            self.assertEqual(mock_out.getvalue(), str(1984) + '\n')
            
            
@patch("sys.stdout", new_callable=StringIO)
def check(obj, res, mock_out):
    scope = Scope()
    Print(obj.evaluate(scope)).evaluate(scope)
    return (mock_out.getvalue() == (str(res) + '\n')) 
    

class TestFunction(unittest.TestCase):
    def test_inst(self):
        assert check((Function(('hello', 'world'), [Number(5), Number(7)])), 7)       
        
        
class TestFunctionDefinition(unittest.TestCase):
    def test_def(self):
        scope = Scope()
        func = Function(('hello', 'world'), [Number(5), Number(7)])
        fdef = FunctionDefinition('myfunc', func)
        fdef.evaluate(scope)
        self.assertIs(scope['myfunc'], func)        


class TestFunctionCall(unittest.TestCase):
    def test_call(self):
        abc = Scope()        
        abc['conditional'] = Function(('a', 'b', 'c', 'd'), 
                         [Conditional(BinaryOperation(Reference('a'), '>', Reference('b')), 
                         [Reference('c')], [Reference('d')])])
        cll = FunctionCall(FunctionDefinition('function', abc['conditional']),
                [Number(4), Number(6), Number(1), Number(777)]).evaluate(abc)
        assert check(cll, 777)

    def test_call_empty(self):
        abc = Scope()        
        abc['haha'] = Function(('a', 'b', 'c', 'd'), [])
        FunctionCall(FunctionDefinition('funct', abc['haha']),
                [Number(4), Number(6), Number(1), Number(777)]).evaluate(abc)


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
     
     
class TestConditional(unittest.TestCase):
    def test_cond(self):
        condition = Conditional(Number(30), [Number(239), Number(404)],
                                  [Number(31), Number(1984)])
        assert check(condition, 404)

        condition = Conditional(Number(0), [Number(123), Number(670)],
                                [Number(100), Number(1998)])
        assert check(condition, 1998)
        
    def test_cond_NoneEmpty(self):
        Conditional(Number(0), [Number(123), Number(670)],
                                None).evaluate(None)   
  
        Conditional(Number(5), None,
                                None).evaluate(None)   
 
        Conditional(Number(0), [], []).evaluate(None)   
  
        Conditional(Number(5), [], []).evaluate(None)   


@patch("sys.stdout", new_callable=StringIO)
def check_logic(obj, res, mock_out):
    scope = Scope()
    Print(obj.evaluate(scope)).evaluate(scope)
    return (bool(int(mock_out.getvalue())) == bool(res)) 

  
class TestBinaryOperation(unittest.TestCase):
    def test_eval(self):    
        
        operations = {"+" : add,
                  "-" : sub,
                  "*" : mul,   
                  "/" : floordiv,
                  "%" : mod}
                  
        log_ops = {"==" : lambda x, y: 1 if x == y else 0,
                  "!=" : lambda x, y: 1 if x != y else 0,
                  "<" : lambda x, y: 1 if x < y else 0,
                  ">" : lambda x, y: 1 if x > y else 0,
                  "<=" : lambda x, y: 1 if x <= y else 0,
                  ">=" : lambda x, y: 1 if x >= y else 0,
                  "&&" : lambda x, y: x and y,  
                  "||" : lambda x, y: x or y}          
        
        
        for a in range(-2, 2):
            for b in range(-2, 2):
                for op, f in operations.items():
                    if b != 0 or (op != '/' and op != '%'):
                        assert check(BinaryOperation(Number(a), op, Number(b)), f(a,b))

        for a in range(-2, 2):
            for b in range(-2, 2):
                for op, f in log_ops.items():
                    assert check_logic(BinaryOperation(Number(a), op, Number(b)), f(a,b))

class TestUnaryOperation(unittest.TestCase):
    def test_eval(self):    
        operations = {"!" : not_,
                      "-" : neg}
    
        for a in range(-2, 2):
            for op, f in operations.items():
                assert check_logic(UnaryOperation(op, Number(a)), f(a))
        

if __name__ == '__main__':
    unittest.main()       
