from operator import (add, truediv, mod, sub, mul, lt, le, not_, gt, ge, ne, eq, neg)

class Scope:
    def __init__(self, parent=None):
        self.parent = parent
        self.d = dict()
    
    def __setitem__(self, key, value):
        self.d[key] = value
    
    def __getitem__(self, key):
        if key not in self.d and self.parent:
            return self.parent[key]
        return self.d[key]    
     

class Number:
    def __init__(self, value):
        self.value = value

    def evaluate(self, scope):
        return self
            
    def __str__(self):
        return "{}".format(self.value)
    
    __repr__ = __str__    


class Function:
    def __init__(self, args, body):
        self.args = args
        self.body = body

    def evaluate(self, scope):
        ans = None
        for op in self.body:
            ans = op.evaluate(scope)
        return ans   


class FunctionDefinition:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def evaluate(self, scope):
        scope[self.name] = self.function
        return self.function


class Conditional:
    def __init__(self, condition, if_true, if_false=None):
        self.condition = condition
        self.if_true = if_true
        self.if_false = if_false

    def evaluate(self, scope):
        ans = None
    
        if self.condition.evaluate(scope).value:
            exprs = self.if_true    
        elif self.if_false is not None:
            exprs = self.if_false
        else:
          return None
          
        for op in exprs:
            ans = op.evaluate(scope)
        return ans    


class Print:
    def __init__(self, expr):
        self.expr = expr

    def evaluate(self, scope):
        res = self.expr.evaluate(scope)        
        print(res.value)
        
        return res


class Read:
    def __init__(self, name):
        self.name = name

    def evaluate(self, scope):
        num = int(input())
        scope[self.name] = Number(num)
        return Number(num)


class FunctionCall:
    def __init__(self, fun_expr, args):
        self.fun_expr = fun_expr
        self.args = args

    def evaluate(self, scope):
        func = self.fun_expr.evaluate(scope)
        call_scope = Scope(scope)
        
        for name, arg in zip(func.args, self.args):
            call_scope[name] = arg.evaluate(scope)
        
        return func.evaluate(call_scope)    
          
          
class Reference:
    def __init__(self, name):
        self.name = name
        
    def evaluate(self, scope):
        return scope[self.name]


class BinaryOperation:
    operations = {"+" : add,
                  "-" : sub,
                  "*" : mul,   
                  "/" : truediv,
                  "%" : mod,
                  "==" : eq,
                  "!=" : ne,
                  "<" : lt,
                  ">" : gt,
                  "<=" : le,
                  ">=" : ge,
                  "&&" : lambda x, y: bool(x and y),  
                  "||" : lambda x, y: bool(x or y)}
        
    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs

    def evaluate(self, scope):
        x = self.lhs.evaluate(scope)
        y = self.rhs.evaluate(scope)
                
        return Number(self.operations[self.op](x.value, y.value))              


class UnaryOperation:
    operations = {"!" : not_,
                  "-" : neg}

    def __init__(self, op, expr):
        self.op = op
        self.expr = expr

    def evaluate(self, scope):
        res = self.expr.evaluate(scope) 
        
        return Number(self.operations[self.op](res.value))


def example():
    parent = Scope()
    parent["foo"] = Function(('hello', 'world'),
                             [Print(BinaryOperation(Reference('hello'),
                                                    '+',
                                                    Reference('world')))])
    parent["bar"] = Number(10)
    scope = Scope(parent)
    assert 10 == scope["bar"].value
    scope["bar"] = Number(20)
    assert scope["bar"].value == 20
    print('It should print 2: ', end=' ')
    FunctionCall(FunctionDefinition('foo', parent['foo']),
                 [Number(5), UnaryOperation('-', Number(3))]).evaluate(scope)


def my_tests():
    abc = Scope()
    abc["func"] = Function(('a', 'b'), 
                            [Print(BinaryOperation(Reference('a'), 
                            '*',
                            Reference('b')))])
    scope = Scope(abs)                        
    scope2 = Scope(scope)
    print('It should print 100 * !0:', end=' ')
    FunctionCall(FunctionDefinition('function', abc['func']),
                 [Number(100), UnaryOperation('!', Number(0))]).evaluate(scope)                        
    
    
    abc["many_args"] = Function(('a', 'b', 'c', 'd', 'e'), 
                                [Print(UnaryOperation('-', Reference('a'))),
                                Print(BinaryOperation(Reference('b'), '<', Reference('d')))])
    print('It should print -3 and (-8 < 7):')
    FunctionCall(FunctionDefinition('function2', abc['many_args']),
                [Number(3), UnaryOperation('-', Number(8)), Number(5), 
                 Number(7), Number(0)]).evaluate(scope2)  
    
    abc["or"] = Function(('a', 'b'),
                            [Print(BinaryOperation(Reference('a'), '||', Reference('b')))])
                            
    print('It should print (0 or 200):')
    FunctionCall(FunctionDefinition('function3', abc['or']),
                [Number(0), Number(200)]).evaluate(scope2)  
                             
    abc['conditional'] = Function(('a', 'b', 'c', 'd'), 
                         [Conditional(BinaryOperation(Reference('a'), '>', Reference('b')), 
                         [Print(Reference('c'))], [Print(Reference('d'))])])
    print('It should print 0 (4 > 6):')                     
    FunctionCall(FunctionDefinition('function4', abc['conditional']),
                [Number(4), Number(6), Number(1), Number(0)]).evaluate(scope2)  
                                 

if __name__ == '__main__':
    #example()
    my_tests()
    pass        
        
