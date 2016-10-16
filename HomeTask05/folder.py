from yat.model import *
from yat.printer import *


class ConstantFolder:
    def visit(self, tree):
        tree = tree.accept(self)
        return tree

    def visitNumber(self, number):
        return number  
        
    def visitReference(self, name):
        return name
    
    def visitBinaryOperation(self, bin_op):
        bin_op.lhs = self.visit(bin_op.lhs)
        bin_op.rhs = self.visit(bin_op.rhs)
            
        if isinstance(bin_op.lhs, Number) and isinstance(bin_op.rhs, Number):
            return bin_op.evaluate(None)
        if isinstance(bin_op.lhs, Number) and isinstance(bin_op.rhs, Reference) and bin_op.lhs.value == 0 and bin_op.op == '*':
            return Number(0)
        if isinstance(bin_op.lhs, Reference) and isinstance(bin_op.rhs, Number) and bin_op.rhs.value == 0 and bin_op.op == '*':
            return Number(0)
        if isinstance(bin_op.lhs, Reference) and isinstance(bin_op.rhs, Reference) and bin_op.lhs == bin_op.rhs and bin_op.op == '-':
            return Number(0)
            
        return bin_op    
        
    def visitUnaryOperation(self, un_op):
        un_op.expr = un_op.expr.accept(self)
        
        if isinstance(un_op.expr, Number):
            return un_op.evaluate(None)
        
        return un_op
        
    def visitPrint(self, prnt):
        prnt.expr = prnt.expr.accept(self)
        return prnt
        
    def visitRead(self, rd):
        return rd

    def visitFunctionDefinition(self, func):        
        for i, expr in enumerate(func.function.body):
            func.function.body[i] = self.visit(expr)
        
        return func

    def visitFunctionCall(self, func):
        for i, arg in enumerate(func.args):
            func.args[i] = arg.accept(self)
            
        return func     
            
    def visitConditional(self, cond):
        cond.condition = cond.condition.accept(self)
        
        if cond.if_true:
            for i, expr in enumerate(cond.if_true):
                cond.if_true[i] = self.visit(expr)

        if cond.if_false:
            for i, expr in enumerate(cond.if_false):
                cond.if_false[i] = self.visit(expr)

        return cond

        
def test():
    c = ConstantFolder()
    p = PrettyPrinter()
    s = BinaryOperation(Number(0), "*", Reference("yy"))
    s = c.visit(s)
    #print(type(s))
    p.visit(s)
    
    
if __name__ == '__main__':
    #test()
    pass    