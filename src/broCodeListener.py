# Generated from broCode.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .broCodeParser import broCodeParser
else:
    from broCodeParser import broCodeParser

# This class defines a complete listener for a parse tree produced by broCodeParser.
class broCodeListener(ParseTreeListener):

    # Enter a parse tree produced by broCodeParser#program.
    def enterProgram(self, ctx:broCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by broCodeParser#program.
    def exitProgram(self, ctx:broCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by broCodeParser#start.
    def enterStart(self, ctx:broCodeParser.StartContext):
        pass

    # Exit a parse tree produced by broCodeParser#start.
    def exitStart(self, ctx:broCodeParser.StartContext):
        pass


    # Enter a parse tree produced by broCodeParser#end.
    def enterEnd(self, ctx:broCodeParser.EndContext):
        pass

    # Exit a parse tree produced by broCodeParser#end.
    def exitEnd(self, ctx:broCodeParser.EndContext):
        pass


    # Enter a parse tree produced by broCodeParser#line.
    def enterLine(self, ctx:broCodeParser.LineContext):
        pass

    # Exit a parse tree produced by broCodeParser#line.
    def exitLine(self, ctx:broCodeParser.LineContext):
        pass


    # Enter a parse tree produced by broCodeParser#statement.
    def enterStatement(self, ctx:broCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by broCodeParser#statement.
    def exitStatement(self, ctx:broCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by broCodeParser#ifBlock.
    def enterIfBlock(self, ctx:broCodeParser.IfBlockContext):
        pass

    # Exit a parse tree produced by broCodeParser#ifBlock.
    def exitIfBlock(self, ctx:broCodeParser.IfBlockContext):
        pass


    # Enter a parse tree produced by broCodeParser#innerBlock.
    def enterInnerBlock(self, ctx:broCodeParser.InnerBlockContext):
        pass

    # Exit a parse tree produced by broCodeParser#innerBlock.
    def exitInnerBlock(self, ctx:broCodeParser.InnerBlockContext):
        pass


    # Enter a parse tree produced by broCodeParser#loopBlock.
    def enterLoopBlock(self, ctx:broCodeParser.LoopBlockContext):
        pass

    # Exit a parse tree produced by broCodeParser#loopBlock.
    def exitLoopBlock(self, ctx:broCodeParser.LoopBlockContext):
        pass


    # Enter a parse tree produced by broCodeParser#block.
    def enterBlock(self, ctx:broCodeParser.BlockContext):
        pass

    # Exit a parse tree produced by broCodeParser#block.
    def exitBlock(self, ctx:broCodeParser.BlockContext):
        pass


    # Enter a parse tree produced by broCodeParser#assignment.
    def enterAssignment(self, ctx:broCodeParser.AssignmentContext):
        pass

    # Exit a parse tree produced by broCodeParser#assignment.
    def exitAssignment(self, ctx:broCodeParser.AssignmentContext):
        pass


    # Enter a parse tree produced by broCodeParser#printstmt.
    def enterPrintstmt(self, ctx:broCodeParser.PrintstmtContext):
        pass

    # Exit a parse tree produced by broCodeParser#printstmt.
    def exitPrintstmt(self, ctx:broCodeParser.PrintstmtContext):
        pass


    # Enter a parse tree produced by broCodeParser#term.
    def enterTerm(self, ctx:broCodeParser.TermContext):
        pass

    # Exit a parse tree produced by broCodeParser#term.
    def exitTerm(self, ctx:broCodeParser.TermContext):
        pass


    # Enter a parse tree produced by broCodeParser#parenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:broCodeParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by broCodeParser#parenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:broCodeParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by broCodeParser#constantExpression.
    def enterConstantExpression(self, ctx:broCodeParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by broCodeParser#constantExpression.
    def exitConstantExpression(self, ctx:broCodeParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by broCodeParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:broCodeParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by broCodeParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:broCodeParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by broCodeParser#identifierExpression.
    def enterIdentifierExpression(self, ctx:broCodeParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by broCodeParser#identifierExpression.
    def exitIdentifierExpression(self, ctx:broCodeParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by broCodeParser#notExpression.
    def enterNotExpression(self, ctx:broCodeParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by broCodeParser#notExpression.
    def exitNotExpression(self, ctx:broCodeParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by broCodeParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:broCodeParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by broCodeParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:broCodeParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by broCodeParser#comparisionExpression.
    def enterComparisionExpression(self, ctx:broCodeParser.ComparisionExpressionContext):
        pass

    # Exit a parse tree produced by broCodeParser#comparisionExpression.
    def exitComparisionExpression(self, ctx:broCodeParser.ComparisionExpressionContext):
        pass


    # Enter a parse tree produced by broCodeParser#booleanExpression.
    def enterBooleanExpression(self, ctx:broCodeParser.BooleanExpressionContext):
        pass

    # Exit a parse tree produced by broCodeParser#booleanExpression.
    def exitBooleanExpression(self, ctx:broCodeParser.BooleanExpressionContext):
        pass


    # Enter a parse tree produced by broCodeParser#constant.
    def enterConstant(self, ctx:broCodeParser.ConstantContext):
        pass

    # Exit a parse tree produced by broCodeParser#constant.
    def exitConstant(self, ctx:broCodeParser.ConstantContext):
        pass



del broCodeParser