from antlr4 import *
from broCodeLexer import broCodeLexer
from broCodeParser import broCodeParser
# from broCodeVisitor import broCodeVisitor
import sys

class broCodeInterpreter(ParseTreeVisitor):
    def __init__(self):
        self.variables = {}

    # Visit a parse tree produced by broCodeParser#program.
    def visitProgram(self, ctx:broCodeParser.ProgramContext):
        for line in ctx.line():
            self.visitLine(line)


    # Visit a parse tree produced by broCodeParser#start.
    def visitStart(self, ctx:broCodeParser.StartContext):
        # return self.visitChildren(ctx)
        pass


    # Visit a parse tree produced by broCodeParser#end.
    def visitEnd(self, ctx:broCodeParser.EndContext):
        # return self.visitChildren(ctx)
        pass


    # Visit a parse tree produced by broCodeParser#line.
    def visitLine(self, ctx:broCodeParser.LineContext):
        if ctx.statement():
            self.visitStatement(ctx.statement())
        elif ctx.ifBlock():
            self.visitIfBlock(ctx.ifBlock())
        elif ctx.loopBlock():
            self.visitLoopBlock(ctx.loopBlock())


    # Visit a parse tree produced by broCodeParser#statement.
    def visitStatement(self, ctx:broCodeParser.StatementContext):
        if ctx.assignment():
            self.visitAssignment(ctx.assignment())
        elif ctx.printstmt():
            self.visitPrintstmt(ctx.printstmt())

    
    def visitIfBlock(self, ctx: broCodeParser.IfBlockContext):
        if self.visit(ctx.expression(0)):
            self.visit(ctx.innerBlock(0))
        else:
            num_elseif = len(ctx.ELSEIF())
            for i in range(num_elseif):
            # evaluate the condition of the ith elseif statement
                if self.visit(ctx.expression(i+1)):
                # execute the inner block of the ith elseif statement
                    self.visit(ctx.innerBlock(i+1))
                    break
            else:
            # execute the inner block of the else statement, if it exists
                if ctx.ELSE():
                    self.visit(ctx.innerBlock(num_elseif+1))




    # Visit a parse tree produced by broCodeParser#innerBlock.
    def visitInnerBlock(self, ctx:broCodeParser.InnerBlockContext):
        if ctx.block():
            self.visitBlock(ctx.block())
        elif ctx.ifBlock():
            self.visitIfBlock(ctx.ifBlock())
        elif ctx.loopBlock():
            self.visitLoopBlock(ctx.loopBlock())


    # Visit a parse tree produced by broCodeParser#loopBlock.
    def visitLoopBlock(self, ctx:broCodeParser.LoopBlockContext):
        while self.visit(ctx.expression()):
            self.visitInnerBlock(ctx.innerBlock())


    # Visit a parse tree produced by broCodeParser#block.
    def visitBlock(self, ctx:broCodeParser.BlockContext):
        for line in ctx.line():
            self.visitLine(line)


    # Visit a parse tree produced by broCodeParser#assignment.
    def visitAssignment(self, ctx:broCodeParser.AssignmentContext):
        identifier = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        self.variables[identifier] = value


    # Visit a parse tree produced by broCodeParser#printstmt.
    def visitPrintstmt(self, ctx:broCodeParser.PrintstmtContext):
        value = self.visit(ctx.term())
        print(value)

    # Visit a parse tree produced by broCodeParser#term.
    def visitTerm(self, ctx:broCodeParser.TermContext):
        if ctx.IDENTIFIER():
            identifier = ctx.IDENTIFIER().getText()
            if identifier not in self.variables:
                raise NameError(f"Undefined variable {identifier}")
            return self.variables[identifier]
        elif ctx.INTEGER():
            return int(ctx.INTEGER().getText())
        elif ctx.STRING():
            return str(ctx.STRING().getText()[1:-1])
        elif ctx.BOOL():
            return ctx.BOOL().getText() == "true"
        elif ctx.NULL():
            return None


    # Visit a parse tree produced by broCodeParser#parenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:broCodeParser.ParenthesizedExpressionContext):
        return self.visit(ctx.expression())


    # Visit a parse tree produced by broCodeParser#constantExpression.
    def visitConstantExpression(self, ctx:broCodeParser.ConstantExpressionContext):
        ct = ctx.constant()
        if ct.INTEGER():
            return int(ct.INTEGER().getText())
        elif ct.FLOAT():
            return float(ct.FLOAT().getText())
        elif ct.STRING:
            return str(ct.STRING().getText()[1:-1])
        elif ct.BOOL:
            return True if ct.BOOL().getText() == 'true' else False
        elif ct.NULL:
            return None


    # Visit a parse tree produced by broCodeParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:broCodeParser.AdditiveExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.ADDOP().getText()
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        else:
            raise Exception(f"Unknown operator: {op}")


    # Visit a parse tree produced by broCodeParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:broCodeParser.IdentifierExpressionContext):
        identifier = ctx.IDENTIFIER().getText()
        return self.variables.get(identifier)


    # Visit a parse tree produced by broCodeParser#notExpression.
    def visitNotExpression(self, ctx:broCodeParser.NotExpressionContext):
        return not self.visit(ctx.expression())


    # Visit a parse tree produced by broCodeParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:broCodeParser.MultiplicativeExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.MULTOP().getText() == '*':
            return left * right
        elif ctx.MULTOP().getText() == '/':
            return left / right
        elif ctx.MULTOP().getText() == '%':
            return left % right


    # Visit a parse tree produced by broCodeParser#comparisionExpression.
    def visitComparisionExpression(self, ctx:broCodeParser.ComparisionExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.COMPAREOP().getText()

        if operator == "==":
            return left == right
        elif operator == "!=":
            return left != right
        elif operator == ">":
            return left > right
        elif operator == ">=":
            return left >= right
        elif operator == "<":
            return left < right
        elif operator == "<=":
            return left <= right


    # Visit a parse tree produced by broCodeParser#booleanExpression.
    def visitBooleanExpression(self, ctx:broCodeParser.BooleanExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.BOOLOP().getText()

        if operator == "and":
            return left and right
        elif operator == "or":
            return left or right
        elif operator == "xor":
            return left != right


    # Visit a parse tree produced by broCodeParser#constant.
    def visitConstant(self, ctx:broCodeParser.ConstantContext):
        ct = ctx.constant()
        if ct.INTEGER() is not None:
            return int(ct.INTEGER().getText())
        elif ct.FLOAT() is not None:
            return float(ct.FLOAT().getText())
        elif ct.STRING() is not None:
            return str(ct.STRING().getText()[1:-1])
        elif ct.BOOL() is not None:
            return ct.BOOL().getText() == 'true'
        elif ct.NULL() is not None:
            return None

def interpret_file(path:str):
    input_stream = FileStream(path)
    lexer = broCodeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = broCodeParser(stream)
    ast = parser.program()
    visitor = broCodeInterpreter()
    visitor.visit(ast)
    
def main():
    if len(sys.argv)>1:
        file = sys.argv[1]
        interpret_file(file)
    else:
        print("Input filename missing")
        
if __name__ == '__main__':
    main()
    