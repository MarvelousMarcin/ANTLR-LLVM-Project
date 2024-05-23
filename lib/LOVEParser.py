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
        4,1,18,79,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,3,
        0,14,8,0,1,0,5,0,17,8,0,10,0,12,0,20,9,0,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,
        2,43,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,54,8,3,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,3,4,64,8,4,1,5,1,5,1,5,1,5,5,5,70,8,5,10,
        5,12,5,73,9,5,3,5,75,8,5,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,0,87,0,
        18,1,0,0,0,2,31,1,0,0,0,4,42,1,0,0,0,6,53,1,0,0,0,8,63,1,0,0,0,10,
        65,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,13,14,1,0,0,0,14,15,1,0,0,
        0,15,17,5,17,0,0,16,13,1,0,0,0,17,20,1,0,0,0,18,16,1,0,0,0,18,19,
        1,0,0,0,19,1,1,0,0,0,20,18,1,0,0,0,21,22,5,8,0,0,22,32,5,9,0,0,23,
        24,5,7,0,0,24,32,5,9,0,0,25,26,5,9,0,0,26,27,5,1,0,0,27,32,3,4,2,
        0,28,29,5,9,0,0,29,30,5,1,0,0,30,32,3,10,5,0,31,21,1,0,0,0,31,23,
        1,0,0,0,31,25,1,0,0,0,31,28,1,0,0,0,32,3,1,0,0,0,33,43,3,6,3,0,34,
        35,3,6,3,0,35,36,5,12,0,0,36,37,3,4,2,0,37,43,1,0,0,0,38,39,3,6,
        3,0,39,40,5,14,0,0,40,41,3,4,2,0,41,43,1,0,0,0,42,33,1,0,0,0,42,
        34,1,0,0,0,42,38,1,0,0,0,43,5,1,0,0,0,44,54,3,8,4,0,45,46,3,8,4,
        0,46,47,5,15,0,0,47,48,3,8,4,0,48,54,1,0,0,0,49,50,3,8,4,0,50,51,
        5,13,0,0,51,52,3,8,4,0,52,54,1,0,0,0,53,44,1,0,0,0,53,45,1,0,0,0,
        53,49,1,0,0,0,54,7,1,0,0,0,55,64,5,11,0,0,56,64,5,10,0,0,57,64,5,
        9,0,0,58,64,5,16,0,0,59,60,5,2,0,0,60,61,3,4,2,0,61,62,5,3,0,0,62,
        64,1,0,0,0,63,55,1,0,0,0,63,56,1,0,0,0,63,57,1,0,0,0,63,58,1,0,0,
        0,63,59,1,0,0,0,64,9,1,0,0,0,65,74,5,4,0,0,66,71,5,11,0,0,67,68,
        5,5,0,0,68,70,5,11,0,0,69,67,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,
        71,72,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,74,66,1,0,0,0,74,75,1,
        0,0,0,75,76,1,0,0,0,76,77,5,6,0,0,77,11,1,0,0,0,8,13,18,31,42,53,
        63,71,74
    ]

class LOVEParser ( Parser ):

    grammarFileName = "LOVE.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'LOVE'", "'('", "')'", "'{'", "','", 
                     "'}'", "'get'", "'show'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'/'", "'-'", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "GET", "SHOW", 
                      "ID", "REAL", "INT", "ADD", "DIV", "MINUS", "MULT", 
                      "STRING", "NEWLINE", "WS" ]

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
    GET=7
    SHOW=8
    ID=9
    REAL=10
    INT=11
    ADD=12
    DIV=13
    MINUS=14
    MULT=15
    STRING=16
    NEWLINE=17
    WS=18

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
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 131968) != 0:
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0:
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
            self.state = 31
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
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = LOVEParser.Single0Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.expr1()
                pass

            elif la_ == 2:
                localctx = LOVEParser.AddContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.expr1()
                self.state = 35
                self.match(LOVEParser.ADD)
                self.state = 36
                self.expr0()
                pass

            elif la_ == 3:
                localctx = LOVEParser.SubstrContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.expr1()
                self.state = 39
                self.match(LOVEParser.MINUS)
                self.state = 40
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
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = LOVEParser.Single1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.expr2()
                pass

            elif la_ == 2:
                localctx = LOVEParser.MultContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.expr2()
                self.state = 46
                self.match(LOVEParser.MULT)
                self.state = 47
                self.expr2()
                pass

            elif la_ == 3:
                localctx = LOVEParser.DivContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.expr2()
                self.state = 50
                self.match(LOVEParser.DIV)
                self.state = 51
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
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = LOVEParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(LOVEParser.INT)
                pass
            elif token in [10]:
                localctx = LOVEParser.RealContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(LOVEParser.REAL)
                pass
            elif token in [9]:
                localctx = LOVEParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.match(LOVEParser.ID)
                pass
            elif token in [16]:
                localctx = LOVEParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.match(LOVEParser.STRING)
                pass
            elif token in [2]:
                localctx = LOVEParser.ParContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 59
                self.match(LOVEParser.T__1)
                self.state = 60
                self.expr0()
                self.state = 61
                self.match(LOVEParser.T__2)
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
            self.state = 65
            self.match(LOVEParser.T__3)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 66
                self.match(LOVEParser.INT)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 67
                    self.match(LOVEParser.T__4)
                    self.state = 68
                    self.match(LOVEParser.INT)
                    self.state = 73
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 76
            self.match(LOVEParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





