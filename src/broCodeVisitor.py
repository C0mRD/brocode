# Generated from broCode.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .broCodeParser import broCodeParser
else:
    from broCodeParser import broCodeParser

# This class defines a complete generic visitor for a parse tree produced by broCodeParser.

class broCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by broCodeParser#program.
    def visitProgram(self, ctx:broCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by broCodeParser#start.
    def visitStart(self, ctx:broCodeParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by broCodeParser#end.
    def visitEnd(self, ctx:broCodeParser.EndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by broCodeParser#line.
    def visitLine(self, ctx:broCodeParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by broCodeParser#statement.
    def visitStatement(self, ctx:broCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by broCodeParser#ifBlock.
    def visitIfBlock(self, ctx:broCodeParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by broCodeParser#innerBlock.
    def visitInnerBlock(self, ctx:broCodeParser.InnerBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by broCodeParser#loopBlock.
    def visitLoopBlock(self, ctx:broCodeParser.LoopBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by broCodeParser#block.
    def visitBlock(self, ctx:broCodeParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by broCodeParser#assignment.
    def visitAssignment(self, ctx:broCodeParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by broCodeParser#printstmt.
    def visitPrintstmt(self, ctx:broCodeParser.PrintstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by broCodeParser#term.
    def visitTerm(self, ctx:broCodeParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by broCodeParser#parenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:broCodeParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by broCodeParser#constantExpression.
    def visitConstantExpression(self, ctx:broCodeParser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by broCodeParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:broCodeParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by broCodeParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:broCodeParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by broCodeParser#notExpression.
    def visitNotExpression(self, ctx:broCodeParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by broCodeParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:broCodeParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by broCodeParser#comparisionExpression.
    def visitComparisionExpression(self, ctx:broCodeParser.ComparisionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by broCodeParser#booleanExpression.
    def visitBooleanExpression(self, ctx:broCodeParser.BooleanExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by broCodeParser#constant.
    def visitConstant(self, ctx:broCodeParser.ConstantContext):
        return self.visitChildren(ctx)



del broCodeParser