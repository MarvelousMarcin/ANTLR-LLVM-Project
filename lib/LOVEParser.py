# Generated from LOVE.g4 by ANTLR 4.11.1
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
        4,1,20,83,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,3,
        0,14,8,0,1,0,5,0,17,8,0,10,0,12,0,20,9,0,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,3,2,47,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,
        58,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,68,8,4,1,5,1,5,1,5,1,
        5,5,5,74,8,5,10,5,12,5,77,9,5,3,5,79,8,5,1,5,1,5,1,5,0,0,6,0,2,4,
        6,8,10,0,0,92,0,18,1,0,0,0,2,35,1,0,0,0,4,46,1,0,0,0,6,57,1,0,0,
        0,8,67,1,0,0,0,10,69,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,13,14,1,
        0,0,0,14,15,1,0,0,0,15,17,5,19,0,0,16,13,1,0,0,0,17,20,1,0,0,0,18,
        16,1,0,0,0,18,19,1,0,0,0,19,1,1,0,0,0,20,18,1,0,0,0,21,22,5,10,0,
        0,22,36,5,11,0,0,23,24,5,9,0,0,24,36,5,11,0,0,25,26,5,11,0,0,26,
        27,5,1,0,0,27,36,3,4,2,0,28,29,5,11,0,0,29,30,5,1,0,0,30,36,3,10,
        5,0,31,32,5,11,0,0,32,33,5,2,0,0,33,34,5,13,0,0,34,36,5,3,0,0,35,
        21,1,0,0,0,35,23,1,0,0,0,35,25,1,0,0,0,35,28,1,0,0,0,35,31,1,0,0,
        0,36,3,1,0,0,0,37,47,3,6,3,0,38,39,3,6,3,0,39,40,5,14,0,0,40,41,
        3,4,2,0,41,47,1,0,0,0,42,43,3,6,3,0,43,44,5,16,0,0,44,45,3,4,2,0,
        45,47,1,0,0,0,46,37,1,0,0,0,46,38,1,0,0,0,46,42,1,0,0,0,47,5,1,0,
        0,0,48,58,3,8,4,0,49,50,3,8,4,0,50,51,5,17,0,0,51,52,3,8,4,0,52,
        58,1,0,0,0,53,54,3,8,4,0,54,55,5,15,0,0,55,56,3,8,4,0,56,58,1,0,
        0,0,57,48,1,0,0,0,57,49,1,0,0,0,57,53,1,0,0,0,58,7,1,0,0,0,59,68,
        5,13,0,0,60,68,5,12,0,0,61,68,5,11,0,0,62,68,5,18,0,0,63,64,5,4,
        0,0,64,65,3,4,2,0,65,66,5,5,0,0,66,68,1,0,0,0,67,59,1,0,0,0,67,60,
        1,0,0,0,67,61,1,0,0,0,67,62,1,0,0,0,67,63,1,0,0,0,68,9,1,0,0,0,69,
        78,5,6,0,0,70,75,5,13,0,0,71,72,5,7,0,0,72,74,5,13,0,0,73,71,1,0,
        0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,79,1,0,0,0,77,75,
        1,0,0,0,78,70,1,0,0,0,78,79,1,0,0,0,79,80,1,0,0,0,80,81,5,8,0,0,
        81,11,1,0,0,0,8,13,18,35,46,57,67,75,78
    ]

class LOVEParser ( Parser ):

    grammarFileName = "LOVE.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'LOVE'", "'['", "']'", "'('", "')'", 
                     "'{'", "','", "'}'", "'get'", "'show'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'/'", "'-'", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "GET", "SHOW", "ID", "REAL", "INT", "ADD", 
                      "DIV", "MINUS", "MULT", "STRING", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr0 = 2
    RULE_expr1 = 3
    RULE_expr2 = 4
    RULE_array = 5

    ruleNames =  [ "prog", "stat", "expr0", "expr1", "expr2", "array" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    GET=9
    SHOW=10
    ID=11
    REAL=12
    INT=13
    ADD=14
    DIV=15
    MINUS=16
    MULT=17
    STRING=18
    NEWLINE=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(LOVEParser.NEWLINE)
            else:
                return self.getToken(LOVEParser.NEWLINE, i)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LOVEParser.StatContext)
            else:
                return self.getTypedRuleContext(LOVEParser.StatContext,i)


        def getRuleIndex(self):
            return LOVEParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = LOVEParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 527872) != 0:
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0:
                    self.state = 12
                    self.stat()


                self.state = 15
                self.match(LOVEParser.NEWLINE)
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LOVEParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignArrayContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LOVEParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LOVEParser.ID, 0)
        def array(self):
            return self.getTypedRuleContext(LOVEParser.ArrayContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignArray" ):
                listener.enterAssignArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignArray" ):
                listener.exitAssignArray(self)


    class GetContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LOVEParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GET(self):
            return self.getToken(LOVEParser.GET, 0)
        def ID(self):
            return self.getToken(LOVEParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGet" ):
                listener.enterGet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGet" ):
                listener.exitGet(self)


    class ShowContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LOVEParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SHOW(self):
            return self.getToken(LOVEParser.SHOW, 0)
        def ID(self):
            return self.getToken(LOVEParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShow" ):
                listener.enterShow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShow" ):
                listener.exitShow(self)


    class ArrayAccessContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LOVEParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LOVEParser.ID, 0)
        def INT(self):
            return self.getToken(LOVEParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAccess" ):
                listener.enterArrayAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAccess" ):
                listener.exitArrayAccess(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LOVEParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LOVEParser.ID, 0)
        def expr0(self):
            return self.getTypedRuleContext(LOVEParser.Expr0Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)



    def stat(self):

        localctx = LOVEParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = LOVEParser.ShowContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.match(LOVEParser.SHOW)
                self.state = 22
                self.match(LOVEParser.ID)
                pass

            elif la_ == 2:
                localctx = LOVEParser.GetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(LOVEParser.GET)
                self.state = 24
                self.match(LOVEParser.ID)
                pass

            elif la_ == 3:
                localctx = LOVEParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.match(LOVEParser.ID)
                self.state = 26
                self.match(LOVEParser.T__0)
                self.state = 27
                self.expr0()
                pass

            elif la_ == 4:
                localctx = LOVEParser.AssignArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.match(LOVEParser.ID)
                self.state = 29
                self.match(LOVEParser.T__0)
                self.state = 30
                self.array()
                pass

            elif la_ == 5:
                localctx = LOVEParser.ArrayAccessContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 31
                self.match(LOVEParser.ID)
                self.state = 32
                self.match(LOVEParser.T__1)
                self.state = 33
                self.match(LOVEParser.INT)
                self.state = 34
                self.match(LOVEParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LOVEParser.RULE_expr0

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Single0Context(Expr0Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LOVEParser.Expr0Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr1(self):
            return self.getTypedRuleContext(LOVEParser.Expr1Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle0" ):
                listener.enterSingle0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle0" ):
                listener.exitSingle0(self)


    class AddContext(Expr0Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LOVEParser.Expr0Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr1(self):
            return self.getTypedRuleContext(LOVEParser.Expr1Context,0)

        def ADD(self):
            return self.getToken(LOVEParser.ADD, 0)
        def expr0(self):
            return self.getTypedRuleContext(LOVEParser.Expr0Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)


    class SubstrContext(Expr0Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LOVEParser.Expr0Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr1(self):
            return self.getTypedRuleContext(LOVEParser.Expr1Context,0)

        def MINUS(self):
            return self.getToken(LOVEParser.MINUS, 0)
        def expr0(self):
            return self.getTypedRuleContext(LOVEParser.Expr0Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubstr" ):
                listener.enterSubstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubstr" ):
                listener.exitSubstr(self)



    def expr0(self):

        localctx = LOVEParser.Expr0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr0)
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = LOVEParser.Single0Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.expr1()
                pass

            elif la_ == 2:
                localctx = LOVEParser.AddContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.expr1()
                self.state = 39
                self.match(LOVEParser.ADD)
                self.state = 40
                self.expr0()
                pass

            elif la_ == 3:
                localctx = LOVEParser.SubstrContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.expr1()
                self.state = 43
                self.match(LOVEParser.MINUS)
                self.state = 44
                self.expr0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LOVEParser.RULE_expr1

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DivContext(Expr1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LOVEParser.Expr1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LOVEParser.Expr2Context)
            else:
                return self.getTypedRuleContext(LOVEParser.Expr2Context,i)

        def DIV(self):
            return self.getToken(LOVEParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiv" ):
                listener.enterDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiv" ):
                listener.exitDiv(self)


    class Single1Context(Expr1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LOVEParser.Expr1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr2(self):
            return self.getTypedRuleContext(LOVEParser.Expr2Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle1" ):
                listener.enterSingle1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle1" ):
                listener.exitSingle1(self)


    class MultContext(Expr1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LOVEParser.Expr1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LOVEParser.Expr2Context)
            else:
                return self.getTypedRuleContext(LOVEParser.Expr2Context,i)

        def MULT(self):
            return self.getToken(LOVEParser.MULT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMult" ):
                listener.enterMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMult" ):
                listener.exitMult(self)



    def expr1(self):

        localctx = LOVEParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr1)
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = LOVEParser.Single1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.expr2()
                pass

            elif la_ == 2:
                localctx = LOVEParser.MultContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.expr2()
                self.state = 50
                self.match(LOVEParser.MULT)
                self.state = 51
                self.expr2()
                pass

            elif la_ == 3:
                localctx = LOVEParser.DivContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.expr2()
                self.state = 54
                self.match(LOVEParser.DIV)
                self.state = 55
                self.expr2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LOVEParser.RULE_expr2

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParContext(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LOVEParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr0(self):
            return self.getTypedRuleContext(LOVEParser.Expr0Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPar" ):
                listener.enterPar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPar" ):
                listener.exitPar(self)


    class StringContext(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LOVEParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(LOVEParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)


    class RealContext(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LOVEParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def REAL(self):
            return self.getToken(LOVEParser.REAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReal" ):
                listener.enterReal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReal" ):
                listener.exitReal(self)


    class IdContext(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LOVEParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LOVEParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class IntContext(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LOVEParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(LOVEParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expr2(self):

        localctx = LOVEParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr2)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                localctx = LOVEParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(LOVEParser.INT)
                pass
            elif token in [12]:
                localctx = LOVEParser.RealContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(LOVEParser.REAL)
                pass
            elif token in [11]:
                localctx = LOVEParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.match(LOVEParser.ID)
                pass
            elif token in [18]:
                localctx = LOVEParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 62
                self.match(LOVEParser.STRING)
                pass
            elif token in [4]:
                localctx = LOVEParser.ParContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 63
                self.match(LOVEParser.T__3)
                self.state = 64
                self.expr0()
                self.state = 65
                self.match(LOVEParser.T__4)
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


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LOVEParser.RULE_array

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArrContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LOVEParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(LOVEParser.INT)
            else:
                return self.getToken(LOVEParser.INT, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArr" ):
                listener.enterArr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArr" ):
                listener.exitArr(self)



    def array(self):

        localctx = LOVEParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array)
        self._la = 0 # Token type
        try:
            localctx = LOVEParser.ArrContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(LOVEParser.T__5)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 70
                self.match(LOVEParser.INT)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 71
                    self.match(LOVEParser.T__6)
                    self.state = 72
                    self.match(LOVEParser.INT)
                    self.state = 77
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 80
            self.match(LOVEParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





