from lib.LOVEParser import LOVEParser
from lib.LOVEListener import LOVEListener

from enum import Enum, auto

class Type(Enum):
    INT = 1
    ID = auto()
    REAL = auto()
    ARRAY = auto()
    STRING = auto()
    UNKNOWN = auto()

class Value:
    def __init__(self, name, type, length, var=""):
       self.name = name
       self.var = var
       self.type = type
       self.length = length
       
    def __str__(self) -> str:
        return f"{self.name} {self.type} {self.length}"

    def getName(self):
        return self.name

class ListenerInterp(LOVEListener):
    text = ""
    header_text =""
    reg = 1
    strr = 1
    
    variables:dict[str, Type] = {}
    stack:list[Value] = []
    
    def __init__(self):
        self.result = {}

    def exitProg(self, ctx: LOVEParser.ProgContext):
        self.generate()
        
    def exitAssign(self, ctx: LOVEParser.AssignContext):
        ID = ctx.ID().getText()
        v:Value = self.stack.pop()
        self.variables[ID] = v.type
        if v.type == Type.INT:
            self.declare_int(ID)
            self.assign_int(ID, v.name)
        if v.type == Type.REAL:
            self.declare_double(ID)
            self.assign_double(ID, v.name)
        if v.type == Type.STRING:
            self.declare_string(ID)
            self.assign_string(ID)
 
    def exitMult(self, ctx: LOVEParser.MultContext):
        v2:Value = self.stack.pop()
        v1:Value = self.stack.pop()

        if(v1.type == v2.type):
            if v1.type == Type.INT: 
                self.mul_i32(v1, v2)
                self.stack.append(Value(f"%{self.reg-1}", Type.INT, 0))  
            if v1.type == Type.REAL:
                self.mul_double(v1, v2)
                self.stack.append(Value(f"%{self.reg-1}", Type.REAL, 0)) 
        else:
            raise TypeError("Mismatch types")
        
    def exitInt(self, ctx: LOVEParser.IntContext):
        self.stack.append(Value(ctx.INT().getText(), Type.INT, 0))

    def exitReal(self, ctx: LOVEParser.RealContext):
        self.stack.append(Value(ctx.REAL().getText(), Type.REAL, 0))
        
    def exitString(self, ctx: LOVEParser.StringContext):
        tmp:str = ctx.STRING().getText()
        content = tmp[1: len(tmp)-1]
        
        self.constant_string(content)
        
        n = f"ptrstr{self.strr-1}"
        self.stack.append(Value(n, Type.STRING, len(content)))


    def exitId(self, ctx: LOVEParser.IdContext):
        if ctx.ID() is not None:
            ID = ctx.ID().getText()
            
            if ID in self.variables:
                if self.variables[ID] == Type.STRING:
                    self.load_string(ID)
                if self.variables[ID] == Type.INT:
                    self.load_i32(ID)
                if self.variables[ID] == Type.REAL:
                    self.load_double(ID)
                self.stack.append(Value(f"%{self.reg-1}", Type.ID, 0, ID))
            
    def exitShow(self, ctx: LOVEParser.ShowContext):
        ID = ctx.ID().getText()
        type = self.variables.get(ID)
        
        if type == Type.INT:
            self.printf_i32(ID)
            
        if type == Type.REAL:
            self.printf_double(ID)
        
        if type == Type.STRING:
            self.printf_string(ID)
            
        
    def exitGet(self, ctx: LOVEParser.GetContext):
        ID = ctx.ID().getText()
        
        if ID not in self.variables:
            self.declare_int(ID)
            self.variables[ID] = Type.INT
            
        self.scanf(ID)
        
    def exitAdd(self, ctx: LOVEParser.AddContext):
        v2:Value = self.stack.pop()
        v1:Value = self.stack.pop()

        if v1.type == Type.ID and v2.type == Type.ID:
            
            if self.variables[v1.var] == Type.INT:
                self.add_int(v1, v2)
                self.stack.append(Value(f"%{self.reg-1}", Type.INT, 0))
                
            elif self.variables[v1.var] == Type.STRING:
                self.add_string(v1.name, v1.length, v2.name, v2.length)
                self.stack.append(Value(f"%{self.reg-3}", Type.STRING, 0))
            else: 
                self.add_double(v1, v2)
                self.stack.append(Value(f"%{self.reg-1}", Type.REAL, 0))
        
        if v1.type == Type.STRING and v2.type == Type.STRING:
            self.add_string(v1.name, v1.length, v2.name, v2.length)
            self.stack.append(Value(f"%{self.reg-3}", Type.STRING, 0))

        
        if v1.type == Type.INT: 
            self.add_int(v1, v2)
            self.stack.append(Value(f"%{self.reg-1}", Type.INT, 0))  
            
        if v1.type == Type.REAL:
            self.add_double(v1, v2)
            self.stack.append(Value(f"%{self.reg-1}", Type.REAL, 0)) 
            
    
    def exitSubstr(self, ctx: LOVEParser.SubstrContext):
        v2:Value = self.stack.pop()
        v1:Value = self.stack.pop()
        
        if v1.type == Type.INT: 
            self.sub_i32(v1, v2)
            self.stack.append(Value(f"%{self.reg-1}", Type.INT, 0))  
        if v1.type == Type.REAL or v1.type == Type.ID:
            self.sub_double(v1, v2)
            self.stack.append(Value(f"%{self.reg-1}", Type.REAL, 0)) 

    def exitDiv(self, ctx: LOVEParser.SubstrContext):
        v2:Value = self.stack.pop()
        v1:Value = self.stack.pop()
        
        if v1.type == Type.INT: 
            self.div_i32(v1, v2)
            self.stack.append(Value(f"%{self.reg-1}", Type.INT, 0))  
        if v1.type == Type.REAL:
            self.div_double(v1, v2)
            self.stack.append(Value(f"%{self.reg-1}", Type.REAL, 0)) 

    def exitAssignArray(self, ctx: LOVEParser.AssignArrayContext):
        print(self.stack.pop())
        
    def exitArr(self, ctx: LOVEParser.ArrContext):
        self.stack.append(Value(ctx.getText(), Type.ARRAY, 0))

                
    def declare_int(self,id):
        self.text += f"%{id} = alloca i32\n"
        
    def declare_double(self,id):
        self.text += f"%{id} = alloca double\n"
        
    def assign_int(self,id, value):
        self.text += f"store i32 {value}, i32* %{id}\n"
  
    def assign_string(self,id, value):
        self.text += f"store i8* %{self.reg-1}, i8** %{id}\n"  
    
    def assign_double(self,id, value):
        self.text += f"store double {value}, double* %{id}\n"
        
    def printf_i32(self,id):
        self.text += f"%{self.reg} = load i32, i32* %{id}\n"
        self.reg += 1
        self.text += f"%{self.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %{self.reg-1})\n"
        self.reg += 1
        
    def printf_double(self,id):
        self.text += f"%{self.reg} = load double, double* %{id}\n"
        self.reg += 1
        self.text += f"%{self.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %{self.reg-1})\n"
        self.reg += 1

    def scanf(self,id):
        self.text += f"%{self.reg} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* %{id})\n"
        self.reg+=1; 
        
    def add_int(self, val1, val2):
        self.text += f"%{self.reg} = add i32 {val1.getName()}, {val2.getName()}\n"
        self.reg += 1
        
    def add_double(self, val1, val2):
        self.text += f"%{self.reg} = fadd double {val1.getName()}, {val2.getName()}\n"
        self.reg += 1
   
    def load_i32(self, id):
        self.text += f"%{self.reg} = load i32, i32* %{id}\n"
        self.reg += 1
        
    def load_double(self, id):
        self.text += f"%{self.reg} = load double, double* %{id}\n"
        self.reg += 1
        
    def sub_i32(self, val1:Value, val2:Value):
        self.text += f"%{self.reg} = sub i32 {val1.getName()}, {val2.getName()}\n"
        self.reg+=1    
     
    def sub_double(self, val1:Value, val2:Value):
        self.text += f"%{self.reg} = fsub double {val1.getName()}, {val2.getName()}\n"
        self.reg+=1  
        
    def div_double(self, val1:Value, val2:Value):
        self.text += f"%{self.reg} = fdiv double {val1.getName()}, {val2.getName()}\n"
        self.reg+=1  
        
    def div_i32(self, val1:Value, val2:Value):
        self.text += f"%{self.reg} = sdiv i32 {val1.getName()}, {val2.getName()}\n"
        self.reg+=1
        
    def mul_i32(self, val1:Value, val2:Value):
        self.text += f"%{self.reg} = mul i32 {val1.getName()}, {val2.getName()}\n"
        self.reg+=1 
       
    def mul_double(self, val1:Value, val2:Value):
        self.text += f"%{self.reg} = fmul double {val1.getName()}, {val2.getName()}\n"
        self.reg+=1    
        
    def scanf(self, id):
        self.text += f"%{self.reg} = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* %{id})\n"
        self.reg += 1
        
    def printf_string(self, id):
        self.text += f"%{self.reg} = load i8*, i8** %{id}\n"
        self.reg += 1
        self.text += f"%{self.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strps, i32 0, i32 0), i8* %{self.reg-1})\n"
        self.reg += 1
        
    def declare_string(self, id):
        self.text += f"%{id} = alloca i8*\n"
        
    def assign_string(self,id):
        self.text += f"store i8* %{self.reg-1}, i8** %{id}\n"
        
    def allocate_string(self,id, l:int):
        self.text += f"%{id} = alloca [{(l+1)*30} x i8]\n"


    def constant_string(self,content:str):
        l = len(content)+1;     
        self.header_text += f"@str{self.strr} = constant [{l} x i8] c\"{content}\\00\"\n"
        n = f"str{self.strr}"
        self.allocate_string(n, (l-1))
        self.text += f"%{self.reg} = bitcast [{l} x i8]* %{n} to i8*\n"
        self.text += f"call void @llvm.memcpy.p0i8.p0i8.i64(i8* align 1 %{self.reg}, i8* align 1 getelementptr inbounds ([{l} x i8], [{l} x i8]* @{n}, i32 0, i32 0), i64 {l}, i1 false)\n"
        self.reg += 1
        self.text += f"%ptr{n} = alloca i8*\n"
        self.text += f"%{self.reg} = getelementptr inbounds [{l} x i8], [{l} x i8]* %{n}, i64 0, i64 0\n"
        self.reg += 1
        self.text += f"store i8* %{self.reg-1}, i8** %ptr{n}\n";    
        self.strr += 1
        
    def add_string(self, id1, l1:int, id2, l2:int):
        self.allocate_string(f"str{self.strr}", l1+l2)
        self.text += f"%ptrstr{self.strr} = alloca i8*\n"
        self.text += f"%{self.reg} = getelementptr inbounds [{l1+l2+1} x i8], [{l1+l2+1} x i8]* %str{self.strr}, i64 0, i64 0\n"
        self.reg +=1
        self.text += f"store i8* %{self.reg-1}, i8** %ptrstr{self.strr}\n" 
        self.text += f"%{self.reg} = load i8*, i8** %ptrstr{self.strr}\n"
        self.reg +=1  
        self.text += f"%{self.reg} = load i8*, i8** %ptrstr{self.strr-2}\n"
        self.reg +=1
        self.text += f"%{self.reg} = call i8* @strcpy(i8* %{self.reg-2}, i8* %{self.reg-1})\n"
        self.reg +=1
        self.text += f"%{self.reg} = load i8*, i8** %ptrstr{self.strr-1}\n"
        self.reg +=1
        self.text += f"%{self.reg} = call i8* @strcat(i8* %{self.reg-4}, i8* %{self.reg-1})\n"
        self.reg +=1
        self.strr += 1 
    
    def load_string(self, id):
        self.text += f"%{self.reg} = load i8*, i8** %{id}\n"
        self.reg += 1
        

        
    def generate(self):
        output = ""
        output += "declare i32 @printf(i8*, ...)\n"
        output += "declare i32 @scanf(ptr noundef, ...) #1\n"
        output += "declare i8* @strcpy(i8*, i8*)\n"
        output += "declare i32 @atoi(i8*)\n"
        output += "declare i8* @strcat(i8*, i8*)\n"
        output += "declare void @llvm.memcpy.p0i8.p0i8.i64(i8* noalias nocapture writeonly, i8* noalias nocapture readonly, i64, i1 immarg)\n"
        output += "@strpi = constant [4 x i8] c\"%d\\0A\\00\"\n"
        output += "@strpd = constant [4 x i8] c\"%f\\0A\\00\"\n"
        output += "@strps = constant [4 x i8] c\"%s\\0A\\00\"\n"
        output += "@strs = constant [3 x i8] c\"%d\\00\"\n"
        output += self.header_text
        output += "define i32 @main() nounwind{\n"
        output += self.text
        output += "ret i32 0 }\n"
        print(output)