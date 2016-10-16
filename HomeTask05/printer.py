from model import *


class PrettyPrinter:
    def __init__(self):
        self.tabs = 0
    
    def visit(self, tree):
        print(self.tabs * "\t", end="")
        tree.accept(self)
        print(";")                    
        
    def visitNumber(self, number):
        print(number, end="")
        
    def visitReference(self, name):
        print(name, end="")
        
    def visitBinaryOperation(self, bin_op):
        print("(", end="")
        bin_op.lhs.accept(self)
        print(") " + bin_op.op + " (", end="")
        bin_op.rhs.accept(self)
        print(")", end="")      
        
    def visitUnaryOperation(self, un_op):
        print("(", end="")
        print(un_op.op, end="")
        un_op.expr.accept(self)
        print(")", end="")      
        
    def visitFunctionDefinition(self, func):
        print("def " + func.name + "(", end="")

        if len(func.function.args) > 0:
            print(func.function.args[0], end="")
        
        for arg in func.function.args[1:]:
            print(", " + arg, end="")
            
        print(") {")
        
        self.tabs += 1
        
        for expr in func.function.body:
            self.visit(expr)
        
        self.tabs -= 1
        print("}", end="")

    def visitFunctionCall(self, func):
        print(func.fun_expr.name + "(", end="")
        
        if len(func.args) > 0:
            func.args[0].accept(self)
     
        for arg in func.args[1:]:
            print(", ", end="")
            arg.accept(self)
            
        print(")", end="")
        
    def visitPrint(self, prnt):
        print("print ", end="")
        prnt.expr.accept(self)

    def visitRead(self, rd):
        print("read ", end="")
        print(rd.name, end="")        

    def visitConditional(self, cond):
        print("if (", end="")
        cond.condition.accept(self)
        print(") {")
        
        self.tabs += 1

        if_tr = []
        if_tr.extend(cond.if_true)
        
        for expr in if_tr:
            self.visit(expr)

        self.tabs -= 1
        
        print("}", end="")

        if cond.if_false:
            print(" else {")
            
            self.tabs += 1
        
            for expr in cond.if_false:
                self.visit(expr)

            self.tabs -= 1
        
            print("}", end="")
