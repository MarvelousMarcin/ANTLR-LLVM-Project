# Generated from LOVE.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LOVEParser import LOVEParser
else:
    from LOVEParser import LOVEParser

# This class defines a complete listener for a parse tree produced by LOVEParser.
class LOVEListener(ParseTreeListener):

    # Enter a parse tree produced by LOVEParser#prog.
    def enterProg(self, ctx:LOVEParser.ProgContext):
        pass

    # Exit a parse tree produced by LOVEParser#prog.
    def exitProg(self, ctx:LOVEParser.ProgContext):
        pass


    # Enter a parse tree produced by LOVEParser#block.
    def enterBlock(self, ctx:LOVEParser.BlockContext):
        pass

    # Exit a parse tree produced by LOVEParser#block.
    def exitBlock(self, ctx:LOVEParser.BlockContext):
        pass


    # Enter a parse tree produced by LOVEParser#function.
    def enterFunction(self, ctx:LOVEParser.FunctionContext):
        pass

    # Exit a parse tree produced by LOVEParser#function.
    def exitFunction(self, ctx:LOVEParser.FunctionContext):
        pass


    # Enter a parse tree produced by LOVEParser#struct.
    def enterStruct(self, ctx:LOVEParser.StructContext):
        pass

    # Exit a parse tree produced by LOVEParser#struct.
    def exitStruct(self, ctx:LOVEParser.StructContext):
        pass


    # Enter a parse tree produced by LOVEParser#structBody.
    def enterStructBody(self, ctx:LOVEParser.StructBodyContext):
        pass

    # Exit a parse tree produced by LOVEParser#structBody.
    def exitStructBody(self, ctx:LOVEParser.StructBodyContext):
        pass


    # Enter a parse tree produced by LOVEParser#showStructMember.
    def enterShowStructMember(self, ctx:LOVEParser.ShowStructMemberContext):
        pass

    # Exit a parse tree produced by LOVEParser#showStructMember.
    def exitShowStructMember(self, ctx:LOVEParser.ShowStructMemberContext):
        pass


    # Enter a parse tree produced by LOVEParser#show.
    def enterShow(self, ctx:LOVEParser.ShowContext):
        pass

    # Exit a parse tree produced by LOVEParser#show.
    def exitShow(self, ctx:LOVEParser.ShowContext):
        pass


    # Enter a parse tree produced by LOVEParser#assignStruct.
    def enterAssignStruct(self, ctx:LOVEParser.AssignStructContext):
        pass

    # Exit a parse tree produced by LOVEParser#assignStruct.
    def exitAssignStruct(self, ctx:LOVEParser.AssignStructContext):
        pass


    # Enter a parse tree produced by LOVEParser#get.
    def enterGet(self, ctx:LOVEParser.GetContext):
        pass

    # Exit a parse tree produced by LOVEParser#get.
    def exitGet(self, ctx:LOVEParser.GetContext):
        pass


    # Enter a parse tree produced by LOVEParser#gets.
    def enterGets(self, ctx:LOVEParser.GetsContext):
        pass

    # Exit a parse tree produced by LOVEParser#gets.
    def exitGets(self, ctx:LOVEParser.GetsContext):
        pass


    # Enter a parse tree produced by LOVEParser#assign.
    def enterAssign(self, ctx:LOVEParser.AssignContext):
        pass

    # Exit a parse tree produced by LOVEParser#assign.
    def exitAssign(self, ctx:LOVEParser.AssignContext):
        pass


    # Enter a parse tree produced by LOVEParser#assignArray.
    def enterAssignArray(self, ctx:LOVEParser.AssignArrayContext):
        pass

    # Exit a parse tree produced by LOVEParser#assignArray.
    def exitAssignArray(self, ctx:LOVEParser.AssignArrayContext):
        pass


    # Enter a parse tree produced by LOVEParser#assignStructMember.
    def enterAssignStructMember(self, ctx:LOVEParser.AssignStructMemberContext):
        pass

    # Exit a parse tree produced by LOVEParser#assignStructMember.
    def exitAssignStructMember(self, ctx:LOVEParser.AssignStructMemberContext):
        pass


    # Enter a parse tree produced by LOVEParser#arrayAccess.
    def enterArrayAccess(self, ctx:LOVEParser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by LOVEParser#arrayAccess.
    def exitArrayAccess(self, ctx:LOVEParser.ArrayAccessContext):
        pass


    # Enter a parse tree produced by LOVEParser#repeat.
    def enterRepeat(self, ctx:LOVEParser.RepeatContext):
        pass

    # Exit a parse tree produced by LOVEParser#repeat.
    def exitRepeat(self, ctx:LOVEParser.RepeatContext):
        pass


    # Enter a parse tree produced by LOVEParser#if.
    def enterIf(self, ctx:LOVEParser.IfContext):
        pass

    # Exit a parse tree produced by LOVEParser#if.
    def exitIf(self, ctx:LOVEParser.IfContext):
        pass


    # Enter a parse tree produced by LOVEParser#blockif.
    def enterBlockif(self, ctx:LOVEParser.BlockifContext):
        pass

    # Exit a parse tree produced by LOVEParser#blockif.
    def exitBlockif(self, ctx:LOVEParser.BlockifContext):
        pass


    # Enter a parse tree produced by LOVEParser#equal.
    def enterEqual(self, ctx:LOVEParser.EqualContext):
        pass

    # Exit a parse tree produced by LOVEParser#equal.
    def exitEqual(self, ctx:LOVEParser.EqualContext):
        pass


    # Enter a parse tree produced by LOVEParser#single0.
    def enterSingle0(self, ctx:LOVEParser.Single0Context):
        pass

    # Exit a parse tree produced by LOVEParser#single0.
    def exitSingle0(self, ctx:LOVEParser.Single0Context):
        pass


    # Enter a parse tree produced by LOVEParser#add.
    def enterAdd(self, ctx:LOVEParser.AddContext):
        pass

    # Exit a parse tree produced by LOVEParser#add.
    def exitAdd(self, ctx:LOVEParser.AddContext):
        pass


    # Enter a parse tree produced by LOVEParser#substr.
    def enterSubstr(self, ctx:LOVEParser.SubstrContext):
        pass

    # Exit a parse tree produced by LOVEParser#substr.
    def exitSubstr(self, ctx:LOVEParser.SubstrContext):
        pass


    # Enter a parse tree produced by LOVEParser#single1.
    def enterSingle1(self, ctx:LOVEParser.Single1Context):
        pass

    # Exit a parse tree produced by LOVEParser#single1.
    def exitSingle1(self, ctx:LOVEParser.Single1Context):
        pass


    # Enter a parse tree produced by LOVEParser#mult.
    def enterMult(self, ctx:LOVEParser.MultContext):
        pass

    # Exit a parse tree produced by LOVEParser#mult.
    def exitMult(self, ctx:LOVEParser.MultContext):
        pass


    # Enter a parse tree produced by LOVEParser#div.
    def enterDiv(self, ctx:LOVEParser.DivContext):
        pass

    # Exit a parse tree produced by LOVEParser#div.
    def exitDiv(self, ctx:LOVEParser.DivContext):
        pass


    # Enter a parse tree produced by LOVEParser#int.
    def enterInt(self, ctx:LOVEParser.IntContext):
        pass

    # Exit a parse tree produced by LOVEParser#int.
    def exitInt(self, ctx:LOVEParser.IntContext):
        pass


    # Enter a parse tree produced by LOVEParser#real.
    def enterReal(self, ctx:LOVEParser.RealContext):
        pass

    # Exit a parse tree produced by LOVEParser#real.
    def exitReal(self, ctx:LOVEParser.RealContext):
        pass


    # Enter a parse tree produced by LOVEParser#float.
    def enterFloat(self, ctx:LOVEParser.FloatContext):
        pass

    # Exit a parse tree produced by LOVEParser#float.
    def exitFloat(self, ctx:LOVEParser.FloatContext):
        pass


    # Enter a parse tree produced by LOVEParser#id.
    def enterId(self, ctx:LOVEParser.IdContext):
        pass

    # Exit a parse tree produced by LOVEParser#id.
    def exitId(self, ctx:LOVEParser.IdContext):
        pass


    # Enter a parse tree produced by LOVEParser#string.
    def enterString(self, ctx:LOVEParser.StringContext):
        pass

    # Exit a parse tree produced by LOVEParser#string.
    def exitString(self, ctx:LOVEParser.StringContext):
        pass


    # Enter a parse tree produced by LOVEParser#par.
    def enterPar(self, ctx:LOVEParser.ParContext):
        pass

    # Exit a parse tree produced by LOVEParser#par.
    def exitPar(self, ctx:LOVEParser.ParContext):
        pass


    # Enter a parse tree produced by LOVEParser#repetitions.
    def enterRepetitions(self, ctx:LOVEParser.RepetitionsContext):
        pass

    # Exit a parse tree produced by LOVEParser#repetitions.
    def exitRepetitions(self, ctx:LOVEParser.RepetitionsContext):
        pass


    # Enter a parse tree produced by LOVEParser#arr.
    def enterArr(self, ctx:LOVEParser.ArrContext):
        pass

    # Exit a parse tree produced by LOVEParser#arr.
    def exitArr(self, ctx:LOVEParser.ArrContext):
        pass


    # Enter a parse tree produced by LOVEParser#fblock.
    def enterFblock(self, ctx:LOVEParser.FblockContext):
        pass

    # Exit a parse tree produced by LOVEParser#fblock.
    def exitFblock(self, ctx:LOVEParser.FblockContext):
        pass


    # Enter a parse tree produced by LOVEParser#fparam.
    def enterFparam(self, ctx:LOVEParser.FparamContext):
        pass

    # Exit a parse tree produced by LOVEParser#fparam.
    def exitFparam(self, ctx:LOVEParser.FparamContext):
        pass



del LOVEParser