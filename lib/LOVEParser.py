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
        4,1,23,108,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,3,0,21,8,0,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,50,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,3,3,61,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,72,8,4,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,82,8,5,1,6,1,6,1,6,1,6,5,6,88,
        8,6,10,6,12,6,91,9,6,3,6,93,8,6,1,6,1,6,1,7,3,7,98,8,7,1,7,5,7,101,
        8,7,10,7,12,7,104,9,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,
        0,118,0,25,1,0,0,0,2,28,1,0,0,0,4,49,1,0,0,0,6,60,1,0,0,0,8,71,1,
        0,0,0,10,81,1,0,0,0,12,83,1,0,0,0,14,102,1,0,0,0,16,105,1,0,0,0,
        18,21,3,4,2,0,19,21,3,2,1,0,20,18,1,0,0,0,20,19,1,0,0,0,20,21,1,
        0,0,0,21,22,1,0,0,0,22,24,5,22,0,0,23,20,1,0,0,0,24,27,1,0,0,0,25,
        23,1,0,0,0,25,26,1,0,0,0,26,1,1,0,0,0,27,25,1,0,0,0,28,29,5,9,0,
        0,29,30,3,16,8,0,30,31,3,14,7,0,31,32,5,10,0,0,32,3,1,0,0,0,33,34,
        5,12,0,0,34,50,5,14,0,0,35,36,5,11,0,0,36,50,5,14,0,0,37,38,5,13,
        0,0,38,50,5,14,0,0,39,40,5,14,0,0,40,41,5,1,0,0,41,50,3,6,3,0,42,
        43,5,14,0,0,43,44,5,1,0,0,44,50,3,12,6,0,45,46,5,14,0,0,46,47,5,
        2,0,0,47,48,5,16,0,0,48,50,5,3,0,0,49,33,1,0,0,0,49,35,1,0,0,0,49,
        37,1,0,0,0,49,39,1,0,0,0,49,42,1,0,0,0,49,45,1,0,0,0,50,5,1,0,0,
        0,51,61,3,8,4,0,52,53,3,8,4,0,53,54,5,17,0,0,54,55,3,6,3,0,55,61,
        1,0,0,0,56,57,3,8,4,0,57,58,5,19,0,0,58,59,3,6,3,0,59,61,1,0,0,0,
        60,51,1,0,0,0,60,52,1,0,0,0,60,56,1,0,0,0,61,7,1,0,0,0,62,72,3,10,
        5,0,63,64,3,10,5,0,64,65,5,20,0,0,65,66,3,10,5,0,66,72,1,0,0,0,67,
        68,3,10,5,0,68,69,5,18,0,0,69,70,3,10,5,0,70,72,1,0,0,0,71,62,1,
        0,0,0,71,63,1,0,0,0,71,67,1,0,0,0,72,9,1,0,0,0,73,82,5,16,0,0,74,
        82,5,15,0,0,75,82,5,14,0,0,76,82,5,21,0,0,77,78,5,4,0,0,78,79,3,
        6,3,0,79,80,5,5,0,0,80,82,1,0,0,0,81,73,1,0,0,0,81,74,1,0,0,0,81,
        75,1,0,0,0,81,76,1,0,0,0,81,77,1,0,0,0,82,11,1,0,0,0,83,92,5,6,0,
        0,84,89,5,16,0,0,85,86,5,7,0,0,86,88,5,16,0,0,87,85,1,0,0,0,88,91,
        1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,
        92,84,1,0,0,0,92,93,1,0,0,0,93,94,1,0,0,0,94,95,5,8,0,0,95,13,1,
        0,0,0,96,98,3,4,2,0,97,96,1,0,0,0,97,98,1,0,0,0,98,99,1,0,0,0,99,
        101,5,22,0,0,100,97,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,
        103,1,0,0,0,103,15,1,0,0,0,104,102,1,0,0,0,105,106,5,14,0,0,106,
        17,1,0,0,0,10,20,25,49,60,71,81,89,92,97,102
    ]

class LOVEParser ( Parser ):

    grammarFileName = "LOVE.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'LOVE'", "'['", "']'", "'('", "')'", 
                     "'{'", "','", "'}'", "'function'", "'endfunction'", 
                     "'get'", "'show'", "'gets'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'/'", "'-'", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "FUNCTION", "ENDFUNCTION", "GET", "SHOW", 
                      "GETS", "ID", "REAL", "INT", "ADD", "DIV", "MINUS", 
                      "MULT", "STRING", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_function = 1
    RULE_stat = 2
    RULE_expr0 = 3
    RULE_expr1 = 4
    RULE_expr2 = 5
    RULE_array = 6
    RULE_fblock = 7
    RULE_fparam = 8

    ruleNames =  [ "prog", "function", "stat", "expr0", "expr1", "expr2", 
                   "array", "fblock", "fparam" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    FUNCTION=9
    ENDFUNCTION=10
    GET=11
    SHOW=12
    GETS=13
    ID=14
    REAL=15
    INT=16
    ADD=17
    DIV=18
    MINUS=19
    MULT=20
    STRING=21
    NEWLINE=22
    WS=23

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


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LOVEParser.FunctionContext)
            else:
                return self.getTypedRuleContext(LOVEParser.FunctionContext,i)


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
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 4225536) != 0:
                self.state = 20
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [11, 12, 13, 14]:
                    self.state = 18
                    self.stat()
                    pass
                elif token in [9]:
                    self.state = 19
                    self.function()
                    pass
                elif token in [22]:
                    pass
                else:
                    pass
                self.state = 22
                self.match(LOVEParser.NEWLINE)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(LOVEParser.FUNCTION, 0)

        def fparam(self):
            return self.getTypedRuleContext(LOVEParser.FparamContext,0)


        def fblock(self):
            return self.getTypedRuleContext(LOVEParser.FblockContext,0)


        def ENDFUNCTION(self):
            return self.getToken(LOVEParser.ENDFUNCTION, 0)

        def getRuleIndex(self):
            return LOVEParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = LOVEParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(LOVEParser.FUNCTION)
            self.state = 29
            self.fparam()
            self.state = 30
            self.fblock()
            self.state = 31
            self.match(LOVEParser.ENDFUNCTION)
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


    class GetsContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LOVEParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GETS(self):
            return self.getToken(LOVEParser.GETS, 0)
        def ID(self):
            return self.getToken(LOVEParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGets" ):
                listener.enterGets(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGets" ):
                listener.exitGets(self)


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
        self.enterRule(localctx, 4, self.RULE_stat)
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = LOVEParser.ShowContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(LOVEParser.SHOW)
                self.state = 34
                self.match(LOVEParser.ID)
                pass

            elif la_ == 2:
                localctx = LOVEParser.GetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(LOVEParser.GET)
                self.state = 36
                self.match(LOVEParser.ID)
                pass

            elif la_ == 3:
                localctx = LOVEParser.GetsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.match(LOVEParser.GETS)
                self.state = 38
                self.match(LOVEParser.ID)
                pass

            elif la_ == 4:
                localctx = LOVEParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 39
                self.match(LOVEParser.ID)
                self.state = 40
                self.match(LOVEParser.T__0)
                self.state = 41
                self.expr0()
                pass

            elif la_ == 5:
                localctx = LOVEParser.AssignArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 42
                self.match(LOVEParser.ID)
                self.state = 43
                self.match(LOVEParser.T__0)
                self.state = 44
                self.array()
                pass

            elif la_ == 6:
                localctx = LOVEParser.ArrayAccessContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 45
                self.match(LOVEParser.ID)
                self.state = 46
                self.match(LOVEParser.T__1)
                self.state = 47
                self.match(LOVEParser.INT)
                self.state = 48
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
        self.enterRule(localctx, 6, self.RULE_expr0)
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = LOVEParser.Single0Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.expr1()
                pass

            elif la_ == 2:
                localctx = LOVEParser.AddContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.expr1()
                self.state = 53
                self.match(LOVEParser.ADD)
                self.state = 54
                self.expr0()
                pass

            elif la_ == 3:
                localctx = LOVEParser.SubstrContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.expr1()
                self.state = 57
                self.match(LOVEParser.MINUS)
                self.state = 58
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
        self.enterRule(localctx, 8, self.RULE_expr1)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = LOVEParser.Single1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.expr2()
                pass

            elif la_ == 2:
                localctx = LOVEParser.MultContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.expr2()
                self.state = 64
                self.match(LOVEParser.MULT)
                self.state = 65
                self.expr2()
                pass

            elif la_ == 3:
                localctx = LOVEParser.DivContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.expr2()
                self.state = 68
                self.match(LOVEParser.DIV)
                self.state = 69
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
        self.enterRule(localctx, 10, self.RULE_expr2)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                localctx = LOVEParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.match(LOVEParser.INT)
                pass
            elif token in [15]:
                localctx = LOVEParser.RealContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.match(LOVEParser.REAL)
                pass
            elif token in [14]:
                localctx = LOVEParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.match(LOVEParser.ID)
                pass
            elif token in [21]:
                localctx = LOVEParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.match(LOVEParser.STRING)
                pass
            elif token in [4]:
                localctx = LOVEParser.ParContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 77
                self.match(LOVEParser.T__3)
                self.state = 78
                self.expr0()
                self.state = 79
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
        self.enterRule(localctx, 12, self.RULE_array)
        self._la = 0 # Token type
        try:
            localctx = LOVEParser.ArrContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(LOVEParser.T__5)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 84
                self.match(LOVEParser.INT)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 85
                    self.match(LOVEParser.T__6)
                    self.state = 86
                    self.match(LOVEParser.INT)
                    self.state = 91
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 94
            self.match(LOVEParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FblockContext(ParserRuleContext):
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
            return LOVEParser.RULE_fblock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFblock" ):
                listener.enterFblock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFblock" ):
                listener.exitFblock(self)




    def fblock(self):

        localctx = LOVEParser.FblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_fblock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 4225024) != 0:
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0:
                    self.state = 96
                    self.stat()


                self.state = 99
                self.match(LOVEParser.NEWLINE)
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FparamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LOVEParser.ID, 0)

        def getRuleIndex(self):
            return LOVEParser.RULE_fparam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFparam" ):
                listener.enterFparam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFparam" ):
                listener.exitFparam(self)




    def fparam(self):

        localctx = LOVEParser.FparamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_fparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(LOVEParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





