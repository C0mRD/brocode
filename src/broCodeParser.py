# Generated from broCode.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,126,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,5,0,31,8,0,10,0,12,0,34,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,
        1,3,1,3,3,3,45,8,3,1,4,1,4,3,4,49,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,5,5,60,8,5,10,5,12,5,63,9,5,1,5,1,5,3,5,67,8,5,1,6,1,6,
        1,6,3,6,72,8,6,1,7,1,7,1,7,1,7,1,8,1,8,5,8,80,8,8,10,8,12,8,83,9,
        8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,3,12,105,8,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,119,8,12,10,12,12,12,
        122,9,12,1,13,1,13,1,13,0,1,24,14,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,0,2,3,0,2,2,4,4,14,14,1,0,2,6,127,0,28,1,0,0,0,2,37,1,0,0,
        0,4,39,1,0,0,0,6,44,1,0,0,0,8,48,1,0,0,0,10,52,1,0,0,0,12,71,1,0,
        0,0,14,73,1,0,0,0,16,77,1,0,0,0,18,86,1,0,0,0,20,90,1,0,0,0,22,93,
        1,0,0,0,24,104,1,0,0,0,26,123,1,0,0,0,28,32,3,2,1,0,29,31,3,6,3,
        0,30,29,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,35,
        1,0,0,0,34,32,1,0,0,0,35,36,3,4,2,0,36,1,1,0,0,0,37,38,5,7,0,0,38,
        3,1,0,0,0,39,40,5,8,0,0,40,5,1,0,0,0,41,45,3,8,4,0,42,45,3,10,5,
        0,43,45,3,14,7,0,44,41,1,0,0,0,44,42,1,0,0,0,44,43,1,0,0,0,45,7,
        1,0,0,0,46,49,3,18,9,0,47,49,3,20,10,0,48,46,1,0,0,0,48,47,1,0,0,
        0,49,50,1,0,0,0,50,51,5,21,0,0,51,9,1,0,0,0,52,53,5,10,0,0,53,54,
        3,24,12,0,54,61,3,12,6,0,55,56,5,12,0,0,56,57,3,24,12,0,57,58,3,
        12,6,0,58,60,1,0,0,0,59,55,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,
        62,1,0,0,0,62,66,1,0,0,0,63,61,1,0,0,0,64,65,5,11,0,0,65,67,3,12,
        6,0,66,64,1,0,0,0,66,67,1,0,0,0,67,11,1,0,0,0,68,72,3,16,8,0,69,
        72,3,10,5,0,70,72,3,14,7,0,71,68,1,0,0,0,71,69,1,0,0,0,71,70,1,0,
        0,0,72,13,1,0,0,0,73,74,5,9,0,0,74,75,3,24,12,0,75,76,3,12,6,0,76,
        15,1,0,0,0,77,81,5,22,0,0,78,80,3,6,3,0,79,78,1,0,0,0,80,83,1,0,
        0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,
        5,23,0,0,85,17,1,0,0,0,86,87,5,14,0,0,87,88,5,15,0,0,88,89,3,24,
        12,0,89,19,1,0,0,0,90,91,5,13,0,0,91,92,3,22,11,0,92,21,1,0,0,0,
        93,94,7,0,0,0,94,23,1,0,0,0,95,96,6,12,-1,0,96,105,3,26,13,0,97,
        105,5,14,0,0,98,99,5,24,0,0,99,100,3,24,12,0,100,101,5,25,0,0,101,
        105,1,0,0,0,102,103,5,16,0,0,103,105,3,24,12,5,104,95,1,0,0,0,104,
        97,1,0,0,0,104,98,1,0,0,0,104,102,1,0,0,0,105,120,1,0,0,0,106,107,
        10,4,0,0,107,108,5,17,0,0,108,119,3,24,12,5,109,110,10,3,0,0,110,
        111,5,18,0,0,111,119,3,24,12,4,112,113,10,2,0,0,113,114,5,19,0,0,
        114,119,3,24,12,3,115,116,10,1,0,0,116,117,5,20,0,0,117,119,3,24,
        12,2,118,106,1,0,0,0,118,109,1,0,0,0,118,112,1,0,0,0,118,115,1,0,
        0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,25,1,0,0,
        0,122,120,1,0,0,0,123,124,7,1,0,0,124,27,1,0,0,0,10,32,44,48,61,
        66,71,81,104,118,120
    ]

class broCodeParser ( Parser ):

    grammarFileName = "broCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'null'", "'start bro\\n'", 
                     "<INVALID>", "'jotokhon bro'", "'jodi bro'", "'na hole bro'", 
                     "'jodi na bro'", "'bol bro'", "<INVALID>", "'->'", 
                     "'!'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "';'", "'{'", "'}'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "WS", "INTEGER", "FLOAT", "STRING", "BOOL", 
                      "NULL", "START", "END", "LOOP", "IF", "ELSE", "ELSEIF", 
                      "PRINT", "IDENTIFIER", "ASSIGN", "NOT", "MULTOP", 
                      "ADDOP", "COMPAREOP", "BOOLOP", "SEMICOLON", "LSECONDPAREN", 
                      "RSECONDPAREN", "LFIRSTPAREN", "RFIRSTPAREN", "COMM" ]

    RULE_program = 0
    RULE_start = 1
    RULE_end = 2
    RULE_line = 3
    RULE_statement = 4
    RULE_ifBlock = 5
    RULE_innerBlock = 6
    RULE_loopBlock = 7
    RULE_block = 8
    RULE_assignment = 9
    RULE_printstmt = 10
    RULE_term = 11
    RULE_expression = 12
    RULE_constant = 13

    ruleNames =  [ "program", "start", "end", "line", "statement", "ifBlock", 
                   "innerBlock", "loopBlock", "block", "assignment", "printstmt", 
                   "term", "expression", "constant" ]

    EOF = Token.EOF
    WS=1
    INTEGER=2
    FLOAT=3
    STRING=4
    BOOL=5
    NULL=6
    START=7
    END=8
    LOOP=9
    IF=10
    ELSE=11
    ELSEIF=12
    PRINT=13
    IDENTIFIER=14
    ASSIGN=15
    NOT=16
    MULTOP=17
    ADDOP=18
    COMPAREOP=19
    BOOLOP=20
    SEMICOLON=21
    LSECONDPAREN=22
    RSECONDPAREN=23
    LFIRSTPAREN=24
    RFIRSTPAREN=25
    COMM=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def start(self):
            return self.getTypedRuleContext(broCodeParser.StartContext,0)


        def end(self):
            return self.getTypedRuleContext(broCodeParser.EndContext,0)


        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(broCodeParser.LineContext)
            else:
                return self.getTypedRuleContext(broCodeParser.LineContext,i)


        def getRuleIndex(self):
            return broCodeParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = broCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.start()
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 26112) != 0):
                self.state = 29
                self.line()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self.end()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START(self):
            return self.getToken(broCodeParser.START, 0)

        def getRuleIndex(self):
            return broCodeParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = broCodeParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(broCodeParser.START)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END(self):
            return self.getToken(broCodeParser.END, 0)

        def getRuleIndex(self):
            return broCodeParser.RULE_end

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnd" ):
                listener.enterEnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnd" ):
                listener.exitEnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnd" ):
                return visitor.visitEnd(self)
            else:
                return visitor.visitChildren(self)




    def end(self):

        localctx = broCodeParser.EndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(broCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(broCodeParser.StatementContext,0)


        def ifBlock(self):
            return self.getTypedRuleContext(broCodeParser.IfBlockContext,0)


        def loopBlock(self):
            return self.getTypedRuleContext(broCodeParser.LoopBlockContext,0)


        def getRuleIndex(self):
            return broCodeParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = broCodeParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_line)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.statement()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.ifBlock()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.loopBlock()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(broCodeParser.SEMICOLON, 0)

        def assignment(self):
            return self.getTypedRuleContext(broCodeParser.AssignmentContext,0)


        def printstmt(self):
            return self.getTypedRuleContext(broCodeParser.PrintstmtContext,0)


        def getRuleIndex(self):
            return broCodeParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = broCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 46
                self.assignment()
                pass
            elif token in [13]:
                self.state = 47
                self.printstmt()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 50
            self.match(broCodeParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(broCodeParser.IF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(broCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(broCodeParser.ExpressionContext,i)


        def innerBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(broCodeParser.InnerBlockContext)
            else:
                return self.getTypedRuleContext(broCodeParser.InnerBlockContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(broCodeParser.ELSEIF)
            else:
                return self.getToken(broCodeParser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(broCodeParser.ELSE, 0)

        def getRuleIndex(self):
            return broCodeParser.RULE_ifBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfBlock" ):
                listener.enterIfBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfBlock" ):
                listener.exitIfBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfBlock" ):
                return visitor.visitIfBlock(self)
            else:
                return visitor.visitChildren(self)




    def ifBlock(self):

        localctx = broCodeParser.IfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(broCodeParser.IF)
            self.state = 53
            self.expression(0)
            self.state = 54
            self.innerBlock()
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 55
                    self.match(broCodeParser.ELSEIF)
                    self.state = 56
                    self.expression(0)
                    self.state = 57
                    self.innerBlock() 
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 64
                self.match(broCodeParser.ELSE)
                self.state = 65
                self.innerBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InnerBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(broCodeParser.BlockContext,0)


        def ifBlock(self):
            return self.getTypedRuleContext(broCodeParser.IfBlockContext,0)


        def loopBlock(self):
            return self.getTypedRuleContext(broCodeParser.LoopBlockContext,0)


        def getRuleIndex(self):
            return broCodeParser.RULE_innerBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInnerBlock" ):
                listener.enterInnerBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInnerBlock" ):
                listener.exitInnerBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInnerBlock" ):
                return visitor.visitInnerBlock(self)
            else:
                return visitor.visitChildren(self)




    def innerBlock(self):

        localctx = broCodeParser.InnerBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_innerBlock)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.block()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.ifBlock()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.loopBlock()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOOP(self):
            return self.getToken(broCodeParser.LOOP, 0)

        def expression(self):
            return self.getTypedRuleContext(broCodeParser.ExpressionContext,0)


        def innerBlock(self):
            return self.getTypedRuleContext(broCodeParser.InnerBlockContext,0)


        def getRuleIndex(self):
            return broCodeParser.RULE_loopBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopBlock" ):
                listener.enterLoopBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopBlock" ):
                listener.exitLoopBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopBlock" ):
                return visitor.visitLoopBlock(self)
            else:
                return visitor.visitChildren(self)




    def loopBlock(self):

        localctx = broCodeParser.LoopBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_loopBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(broCodeParser.LOOP)
            self.state = 74
            self.expression(0)
            self.state = 75
            self.innerBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSECONDPAREN(self):
            return self.getToken(broCodeParser.LSECONDPAREN, 0)

        def RSECONDPAREN(self):
            return self.getToken(broCodeParser.RSECONDPAREN, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(broCodeParser.LineContext)
            else:
                return self.getTypedRuleContext(broCodeParser.LineContext,i)


        def getRuleIndex(self):
            return broCodeParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = broCodeParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(broCodeParser.LSECONDPAREN)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 26112) != 0):
                self.state = 78
                self.line()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(broCodeParser.RSECONDPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(broCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(broCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(broCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return broCodeParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = broCodeParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(broCodeParser.IDENTIFIER)
            self.state = 87
            self.match(broCodeParser.ASSIGN)
            self.state = 88
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(broCodeParser.PRINT, 0)

        def term(self):
            return self.getTypedRuleContext(broCodeParser.TermContext,0)


        def getRuleIndex(self):
            return broCodeParser.RULE_printstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintstmt" ):
                listener.enterPrintstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintstmt" ):
                listener.exitPrintstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintstmt" ):
                return visitor.visitPrintstmt(self)
            else:
                return visitor.visitChildren(self)




    def printstmt(self):

        localctx = broCodeParser.PrintstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_printstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(broCodeParser.PRINT)
            self.state = 91
            self.term()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(broCodeParser.IDENTIFIER, 0)

        def INTEGER(self):
            return self.getToken(broCodeParser.INTEGER, 0)

        def STRING(self):
            return self.getToken(broCodeParser.STRING, 0)

        def getRuleIndex(self):
            return broCodeParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = broCodeParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16404) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return broCodeParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParenthesizedExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a broCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LFIRSTPAREN(self):
            return self.getToken(broCodeParser.LFIRSTPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(broCodeParser.ExpressionContext,0)

        def RFIRSTPAREN(self):
            return self.getToken(broCodeParser.RFIRSTPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesizedExpression" ):
                listener.enterParenthesizedExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesizedExpression" ):
                listener.exitParenthesizedExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesizedExpression" ):
                return visitor.visitParenthesizedExpression(self)
            else:
                return visitor.visitChildren(self)


    class ConstantExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a broCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def constant(self):
            return self.getTypedRuleContext(broCodeParser.ConstantContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantExpression" ):
                listener.enterConstantExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantExpression" ):
                listener.exitConstantExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantExpression" ):
                return visitor.visitConstantExpression(self)
            else:
                return visitor.visitChildren(self)


    class AdditiveExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a broCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(broCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(broCodeParser.ExpressionContext,i)

        def ADDOP(self):
            return self.getToken(broCodeParser.ADDOP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a broCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(broCodeParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierExpression" ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierExpression" ):
                listener.exitIdentifierExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierExpression" ):
                return visitor.visitIdentifierExpression(self)
            else:
                return visitor.visitChildren(self)


    class NotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a broCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(broCodeParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(broCodeParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpression" ):
                listener.enterNotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpression" ):
                listener.exitNotExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpression" ):
                return visitor.visitNotExpression(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicativeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a broCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(broCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(broCodeParser.ExpressionContext,i)

        def MULTOP(self):
            return self.getToken(broCodeParser.MULTOP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)


    class ComparisionExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a broCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(broCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(broCodeParser.ExpressionContext,i)

        def COMPAREOP(self):
            return self.getToken(broCodeParser.COMPAREOP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisionExpression" ):
                listener.enterComparisionExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisionExpression" ):
                listener.exitComparisionExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisionExpression" ):
                return visitor.visitComparisionExpression(self)
            else:
                return visitor.visitChildren(self)


    class BooleanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a broCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(broCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(broCodeParser.ExpressionContext,i)

        def BOOLOP(self):
            return self.getToken(broCodeParser.BOOLOP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanExpression" ):
                listener.enterBooleanExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanExpression" ):
                listener.exitBooleanExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanExpression" ):
                return visitor.visitBooleanExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = broCodeParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 5, 6]:
                localctx = broCodeParser.ConstantExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 96
                self.constant()
                pass
            elif token in [14]:
                localctx = broCodeParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 97
                self.match(broCodeParser.IDENTIFIER)
                pass
            elif token in [24]:
                localctx = broCodeParser.ParenthesizedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 98
                self.match(broCodeParser.LFIRSTPAREN)
                self.state = 99
                self.expression(0)
                self.state = 100
                self.match(broCodeParser.RFIRSTPAREN)
                pass
            elif token in [16]:
                localctx = broCodeParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 102
                self.match(broCodeParser.NOT)
                self.state = 103
                self.expression(5)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 120
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 118
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = broCodeParser.MultiplicativeExpressionContext(self, broCodeParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 106
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 107
                        self.match(broCodeParser.MULTOP)
                        self.state = 108
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = broCodeParser.AdditiveExpressionContext(self, broCodeParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 109
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 110
                        self.match(broCodeParser.ADDOP)
                        self.state = 111
                        self.expression(4)
                        pass

                    elif la_ == 3:
                        localctx = broCodeParser.ComparisionExpressionContext(self, broCodeParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 112
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 113
                        self.match(broCodeParser.COMPAREOP)
                        self.state = 114
                        self.expression(3)
                        pass

                    elif la_ == 4:
                        localctx = broCodeParser.BooleanExpressionContext(self, broCodeParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 115
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 116
                        self.match(broCodeParser.BOOLOP)
                        self.state = 117
                        self.expression(2)
                        pass

             
                self.state = 122
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(broCodeParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(broCodeParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(broCodeParser.STRING, 0)

        def BOOL(self):
            return self.getToken(broCodeParser.BOOL, 0)

        def NULL(self):
            return self.getToken(broCodeParser.NULL, 0)

        def getRuleIndex(self):
            return broCodeParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = broCodeParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 124) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




