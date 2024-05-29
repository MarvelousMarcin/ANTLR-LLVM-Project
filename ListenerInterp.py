from lib.LOVEParser import LOVEParser
from lib.LOVEListener import LOVEListener

from enum import Enum, auto

class Type(Enum):
    INT = 1
    ID = auto()
    REAL = auto()
    ARRAY = auto()
    STRING = auto()
    FUNCTION = auto()
    UNKNOWN = auto()
    STRUCT = auto()  # Added STRUCT type

class Value:
    def __init__(self, name, type, length, var="", elements=[], members={}):
       self.name = name
       self.var = var
       self.type = type
       self.length = length
       self.elements = elements
       self.members = members  # Added members for struct fields
       
    def __str__(self) -> str:
        return f"{self.name} {self.type} {self.length}"

    def getName(self):
        return self.name

class ListenerInterp(LOVEListener):
    text = ""
    header_text =""
    reg = 1
    strr = 1
    main_tmp = 1
    br = 0
    brstack = []
    structs = {}  # Store struct definitions
    str_tmp = 0
    
    variables:dict[str, Type] = {}
    localnames: dict[str, Type] = {}
    stack:list[Value] = []
    function:str = ""
    functions = {}
    buffer = ""
    glob = True
    
    def __init__(self):
        self.result = {}

    def enterProg(self, ctx: LOVEParser.ProgContext):
        self.glob = True

    def exitProg(self, ctx: LOVEParser.ProgContext):
        self.close_main()
        self.generate()
        
    def set_variable(self, ID: str, type: Type):
        id = ""
        if self.glob :
            if ID not in self.variables:
                if type == Type.INT:
                    self.variables[ID] = Type.INT
                    self.declare_int(ID, True)
                if type == Type.REAL:
                    self.variables[ID] = Type.REAL
                    self.declare_double(ID, True)
            id = f"@{ID}"
        elif not self.glob:
            if ID not in self.localnames:
                if type == Type.INT:
                    self.localnames[ID] = Type.INT
                    self.declare_int(ID, False)
            id = f"%{ID}" 
        return id
        
    def exitAssign(self, ctx: LOVEParser.AssignContext):
        ID = ctx.ID().getText()

        v:Value = self.stack.pop()
        if v.type == Type.INT:
            self.assign_int(self.set_variable(ID, Type.INT), v.name)
        elif v.type == Type.REAL:
            self.assign_double(self.set_variable(ID, Type.REAL), v.name)
        elif v.type == Type.STRING:
            if ID not in self.variables:
                self.declare_string(ID)
            self.assign_string(ID)
 
    def exitMult(self, ctx: LOVEParser.MultContext):
        v2:Value = self.stack.pop()
        v1:Value = self.stack.pop()

        if v1.type == Type.ID or v2.type == Type.ID:
            if v1.type == Type.ID :
                if self.variables[v1.var] == Type.INT:
                    self.mul_i32(v1, v2)
                    self.stack.append(Value(f"%{self.reg-1}", Type.INT, 0))
                else: 
                    self.mul_double(v1, v2)
                    self.stack.append(Value(f"%{self.reg-1}", Type.REAL, 0))
            if v2.type == Type.ID:
                if self.variables[v2.var] == Type.INT:
                    self.mul_i32(v1, v2)
                    self.stack.append(Value(f"%{self.reg-1}", Type.INT, 0))
                else: 
                    self.mul_double(v1, v2)
                    self.stack.append(Value(f"%{self.reg-1}", Type.REAL, 0))

        elif v1.type != v2.type:
            raise TypeError(f"Different type multiplication")

        elif v1.type == Type.INT: 
            self.mul_i32(v1, v2)
            self.stack.append(Value(f"%{self.reg-1}", Type.INT, 0))  
        elif v1.type == Type.REAL:
            self.mul_double(v1, v2)
            self.stack.append(Value(f"%{self.reg-1}", Type.REAL, 0)) 
        
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

    def exitFparam(self, ctx: LOVEParser.FparamContext):
        ID = ctx.ID().getText()
        self.functions[ID] = ID
        self.function = ID
        self.functionstart(ID)

    def enterFblock(self, ctx: LOVEParser.FblockContext):
        self.glob = False

    def exitFblock(self, ctx: LOVEParser.FblockContext):
        if self.function not in self.localnames:
            self.assign_int(self.set_variable(self.function, Type.INT), 0)
        
        self.load_i32(f"%{self.function}")
        self.functionend()
        self.localnames = {}
        self.glob = True

    def exitArrayAccess(self, ctx: LOVEParser.ArrayAccessContext):
        ID = ctx.ID().getText()
        index = int(ctx.INT().getText())

        if ID in self.variables and self.variables[ID] == Type.ARRAY:
            array_value = self.stack.pop()
            element = array_value.elements[index]

            if isinstance(element, int):
                self.print_int_element(element)
        else:
            print(f"Error: Array '{ID}' is not defined or not of type ARRAY")

    def exitAssignStructMember(self, ctx:LOVEParser.AssignStructMemberContext):
        struct_name = ctx.ID(0).getText()
        instance_name = ctx.ID(1).getText()
        
        struct = self.structs[struct_name.title()]
        index_val = struct.index(instance_name)

        v:Value = self.stack.pop()
        self.buffer += f"%{struct_name+"_"+instance_name} = getelementptr inbounds %struct.{"Person"}, ptr %{struct_name}, i32 0, i32 {index_val}\n"
        self.buffer += f"store i32 {v.name}, ptr %{struct_name+"_"+instance_name}\n"
        
    def exitShowStructMember(self, ctx:LOVEParser.ShowStructMemberContext):
        struct_name = ctx.ID(0).getText()
        instance_name = ctx.ID(1).getText()
        
        struct = self.structs[struct_name.title()]
        index_val = struct.index(instance_name)
        
        self.buffer += f"%{self.reg} = getelementptr inbounds %struct.Person, ptr %{struct_name}, i32 0, i32 {index_val}\n"
        self.reg += 1
        self.buffer += f"%{self.reg} = load i32, ptr %{self.reg-1}, align 4\n"
        self.reg += 1
        self.buffer += f"%{self.reg} = call i32 (ptr, ...) @printf(ptr noundef @.str, i32 noundef %{self.reg-1})\n"
        self.reg += 1

    def enterStruct(self, ctx: LOVEParser.StructContext):
        struct_name = ctx.ID().getText()
        self.structs[struct_name] = []

    def exitStructBody(self, ctx: LOVEParser.StructBodyContext):
        struct_name = ctx.parentCtx.ID().getText()
        members = []
        for member in ctx.ID():
            members.append(member.getText())
        self.structs[struct_name] = members

        # Generate LLVM struct type definition
        struct_type = f"%struct.{struct_name} = type {{ "
        struct_type += ', '.join(["i32" for _ in self.structs[struct_name]])  # Assuming all members are i32 for simplicity
        struct_type += " }"
        self.header_text += struct_type + "\n"
        
    def exitAssignStruct(self, ctx: LOVEParser.AssignStructContext):
        struct_name = ctx.ID(0).getText()
        instance_name = ctx.ID(1).getText()
        if struct_name in self.structs:
            members = {member: None for member in self.structs[struct_name]}
            self.variables[instance_name] = Type.STRUCT
            self.stack.append(Value(instance_name, Type.STRUCT, 0, members=members))

            # Allocate memory for struct instance
            self.buffer += f"%{instance_name} = alloca %struct.{struct_name}\n"
        else:
            raise ValueError(f"Struct {struct_name} is not defined.")

    def exitId(self, ctx: LOVEParser.IdContext):
        if ctx.ID() is not None:
            ID = ctx.ID().getText()
            if ID in self.functions:
                self.call(ID)
                self.stack.append(Value(f"%{self.reg-1}", Type.INT, 0, ID))

            if ID in self.localnames:
                if self.localnames[ID] == Type.INT:
                    self.load_i32(f"%{ID}")
                self.stack.append(Value(f"%{self.reg-1}", Type.INT, 0, ID))
                
            if ID in self.variables:
                if self.variables[ID] == Type.STRING:
                    self.load_string(f"{ID}")
                if self.variables[ID] == Type.INT:
                    self.load_i32(f"@{ID}")
                if self.variables[ID] == Type.REAL:
                    self.load_double(f"@{ID}")
                self.stack.append(Value(f"%{self.reg-1}", Type.ID, 0, ID))
            
    def exitShow(self, ctx: LOVEParser.ShowContext):
        ID = ctx.ID().getText()
        type = self.variables.get(ID)
        prefix = "@"
        
        if not type:
            type = self.localnames.get(ID)
            prefix = "%"

        if type == Type.INT:
            self.printf_i32(f"{prefix}{ID}")
        elif type == Type.REAL:
            self.printf_double(f"{prefix}{ID}")
        elif type == Type.STRING:
            self.printf_string(f"{prefix}{ID}")
        elif type == Type.ARRAY:
            self.show_array(ID)
        else:
            raise TypeError(f"No variable {ID} exists")

      
    def exitGets(self, ctx: LOVEParser.GetsContext):
        ID = ctx.ID().getText()
        self.variables[ID] = Type.STRING
        self.scanf_string(ID, 16)     
        
    def exitGet(self, ctx: LOVEParser.GetContext):
        ID = ctx.ID().getText()
        self.scanf(self.set_variable(ID, Type.INT))
        
    def exitAdd(self, ctx: LOVEParser.AddContext):
        v2:Value = self.stack.pop()
        v1:Value = self.stack.pop()
        
        if v1.type == Type.ID:
            
            if self.variables[v1.var] == Type.INT:
                self.add_int(v1, v2)
                self.stack.append(Value(f"%{self.reg-1}", Type.INT, 0))
                
            elif self.variables[v1.var] == Type.STRING:
                self.add_string(v1.name, v1.length, v2.name, v2.length)
                self.stack.append(Value(f"%{self.reg-3}", Type.STRING, 0))
            else: 
                self.add_double(v1, v2)
                self.stack.append(Value(f"%{self.reg-1}", Type.REAL, 0))
        
        elif v1.type == Type.STRING and v2.type == Type.STRING:
            self.add_string(v1.name, v1.length, v2.name, v2.length)
            self.stack.append(Value(f"%{self.reg-3}", Type.STRING, 0))
        elif v1.type != v2.type:
            raise TypeError(f"Different type addition")    
        elif v1.type == Type.INT: 
            self.add_int(v1, v2)
            self.stack.append(Value(f"%{self.reg-1}", Type.INT, 0))  
            
        elif v1.type == Type.REAL:
            self.add_double(v1, v2)
            self.stack.append(Value(f"%{self.reg-1}", Type.REAL, 0)) 
       
    def enterBlockif(self, ctx: LOVEParser.BlockifContext):
        self.ifstart()
        
    def exitBlockif(self, ctx: LOVEParser.BlockifContext):
        self.ifend()
        
    def exitEqual(self, ctx: LOVEParser.EqualContext):
        ID = ctx.ID().getText()
        INT = ctx.INT().getText()
        prefix = ""
        if ID in self.variables:
            prefix = "@"
        if ID in self.localnames:
            prefix = "%"
        self.icmp(f"{prefix}{ID}", INT)
    
    def exitSubstr(self, ctx: LOVEParser.SubstrContext):
        v2:Value = self.stack.pop()
        v1:Value = self.stack.pop()
        
        if v1.type == Type.ID or v2.type == Type.ID:
            
            if v1.type == Type.ID and v2.type == Type.ID:
                self.sub_i32(v1, v2)
                self.stack.append(Value(f"%{self.reg-1}", Type.INT, 0))
            elif v1.type == Type.ID:
                if self.variables[v1.var] == Type.INT:
                    self.sub_i32(v1, v2)
                    self.stack.append(Value(f"%{self.reg-1}", Type.INT, 0))
                else: 
                    self.sub_double(v1, v2)
                    self.stack.append(Value(f"%{self.reg-1}", Type.REAL, 0))
            elif v2.type == Type.ID:
                if self.variables[v2.var] == Type.INT:
                    self.sub_i32(v1, v2)
                    self.stack.append(Value(f"%{self.reg-1}", Type.INT, 0))
                else: 
                    self.sub_double(v1, v2)
                    self.stack.append(Value(f"%{self.reg-1}", Type.REAL, 0))
                    
        elif v1.type != v2.type:
            raise TypeError(f"Different type substraction")    
        elif v1.type == Type.INT: 
            self.sub_i32(v1, v2)
            self.stack.append(Value(f"%{self.reg-1}", Type.INT, 0))  
            print("ENTER")
        elif v1.type == Type.REAL or v1.type == Type.ID:
            self.sub_double(v1, v2)
            self.stack.append(Value(f"%{self.reg-1}", Type.REAL, 0)) 

    def exitDiv(self, ctx: LOVEParser.SubstrContext):
        v2:Value = self.stack.pop()
        v1:Value = self.stack.pop()

        if v1.type == Type.ID or v2.type == Type.ID:
            
            if v1.type == Type.ID :
                if self.variables[v1.var] == Type.INT:
                    self.div_i32(v1, v2)
                    self.stack.append(Value(f"%{self.reg-1}", Type.INT, 0))
                else: 
                    self.div_double(v1, v2)
                    self.stack.append(Value(f"%{self.reg-1}", Type.REAL, 0))
            elif v2.type == Type.ID:
                if self.variables[v2.var] == Type.INT:
                    self.div_i32(v1, v2)
                    self.stack.append(Value(f"%{self.reg-1}", Type.INT, 0))
                else: 
                    self.div_double(v1, v2)
                    self.stack.append(Value(f"%{self.reg-1}", Type.REAL, 0))
        
        elif v1.type != v2.type:
            raise TypeError(f"Different type division")
        elif v1.type == Type.INT: 
            self.div_i32(v1, v2)
            self.stack.append(Value(f"%{self.reg-1}", Type.INT, 0))  
        elif v1.type == Type.REAL:
            self.div_double(v1, v2)
            self.stack.append(Value(f"%{self.reg-1}", Type.REAL, 0)) 

    def exitRepetitions(self, ctx:LOVEParser.RepetitionsContext):
        v = self.stack.pop()            
        self.repeatstart(v.name)
        
    def exitBlock(self, ctx: LOVEParser.BlockContext):
        if isinstance(ctx.parentCtx, LOVEParser.RepeatContext):
            self.repeatend()

    def exitAssignArray(self, ctx: LOVEParser.AssignArrayContext):
        ID = ctx.ID().getText()
        v = self.stack.pop()
        array_values = v.name[1:-1].split(",")
        elements = [int(v.strip()) for v in array_values]
        array_length = len(elements)
        array_value = Value(ID, Type.ARRAY, array_length, elements=elements)
        
        self.variables[ID] = Type.ARRAY
        self.stack.append(array_value)
        self.declare_int_array(ID, array_length)
        
        for i, element in enumerate(elements):
            self.assign_int_array_element(ID, i, element)
        
    def exitArr(self, ctx: LOVEParser.ArrContext):
        self.stack.append(Value(ctx.getText(), Type.ARRAY, 0))

    def declare_int_array(self, id, length):
        self.buffer += f"%{id} = alloca [{length} x i32]\n"

    def assign_int_array_element(self, id, index, value):
        self.buffer += f"%{self.reg} = getelementptr inbounds [{index+1} x i32], [{index+1} x i32]* %{id}, i32 0, i32 {index}\n"
        self.reg += 1
        self.buffer += f"store i32 {value}, i32* %{self.reg-1}\n"
                
    def declare_int(self,id, glob=False):
        if glob:
            self.header_text += f"@{id} = global i32 0\n"
        else:
            self.buffer += f"%{id} = alloca i32\n"
        
    def declare_double(self,id, glob=False):
        if glob:
            self.header_text += f"@{id} = global double 0.0\n"
        else:
            self.buffer += f"%{id} = alloca double\n"
        
    def assign_int(self,id, value):
        self.buffer += f"store i32 {value}, i32* {id}\n"
  
    def assign_string(self,id, value):
        self.buffer += f"store i8* %{self.reg-1}, i8** %{id}\n"  
    
    def assign_double(self,id, value):
        self.buffer += f"store double {value}, double* {id}\n"
        
    def printf_i32(self,id):
        self.buffer += f"%{self.reg} = load i32, i32* {id}\n"
        self.reg += 1
        self.buffer += f"%{self.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %{self.reg-1})\n"
        self.reg += 1
        
    def printf_double(self,id):
        self.buffer += f"%{self.reg} = load double, double* {id}\n"
        self.reg += 1
        self.buffer += f"%{self.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %{self.reg-1})\n"
        self.reg += 1

    def add_int(self, val1, val2):
        self.buffer += f"%{self.reg} = add i32 {val1.getName()}, {val2.getName()}\n"
        self.reg += 1
        
    def add_int_simple(self, val1, val2):
        self.buffer += f"%{self.reg} = add i32 {val1}, {val2}\n"
        self.reg += 1
        
    def add_double(self, val1, val2):
        self.buffer += f"%{self.reg} = fadd double {val1.getName()}, {val2.getName()}\n"
        self.reg += 1
   
    def load_i32(self, id):
        self.buffer += f"%{self.reg} = load i32, i32* {id}\n"
        self.reg += 1
        
    def load_double(self, id):
        self.buffer += f"%{self.reg} = load double, double* {id}\n"
        self.reg += 1
        
    def sub_i32(self, val1:Value, val2:Value):
        self.buffer += f"%{self.reg} = sub i32 {val1.getName()}, {val2.getName()}\n"
        self.reg+=1    
     
    def sub_double(self, val1:Value, val2:Value):
        self.buffer += f"%{self.reg} = fsub double {val1.getName()}, {val2.getName()}\n"
        self.reg+=1  
        
    def div_double(self, val1:Value, val2:Value):
        self.buffer += f"%{self.reg} = fdiv double {val1.getName()}, {val2.getName()}\n"
        self.reg+=1  
        
    def div_i32(self, val1:Value, val2:Value):
        self.buffer += f"%{self.reg} = sdiv i32 {val1.getName()}, {val2.getName()}\n"
        self.reg+=1
        
    def mul_i32(self, val1:Value, val2:Value):
        self.buffer += f"%{self.reg} = mul i32 {val1.getName()}, {val2.getName()}\n"
        self.reg+=1 
       
    def mul_double(self, val1:Value, val2:Value):
        self.buffer += f"%{self.reg} = fmul double {val1.getName()}, {val2.getName()}\n"
        self.reg+=1    
        
    def scanf(self, id):
        self.buffer += f"%{self.reg} = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* {id})\n"
        self.reg += 1
        
    def printf_string(self, id):
        self.buffer += f"%{self.reg} = load i8*, i8** %{id}\n"
        self.reg += 1
        self.buffer += f"%{self.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strps, i32 0, i32 0), i8* %{self.reg-1})\n"
        self.reg += 1
        
    def declare_string(self, id):
        self.buffer += f"%{id} = alloca i8*\n"
        
    def assign_string(self,id):
        self.buffer += f"store i8* %{self.reg-1}, i8** %{id}\n"
        
    def allocate_string(self,id, l:int):
        self.buffer += f"%{id} = alloca [{(l+1)*30} x i8]\n"


    def constant_string(self,content:str):
        l = len(content)+1;     
        self.header_text += f"@str{self.strr} = constant [{l} x i8] c\"{content}\\00\"\n"
        n = f"str{self.strr}"
        self.allocate_string(n, (l-1))
        self.buffer += f"%{self.reg} = bitcast [{l} x i8]* %{n} to i8*\n"
        self.buffer += f"call void @llvm.memcpy.p0i8.p0i8.i64(i8* align 1 %{self.reg}, i8* align 1 getelementptr inbounds ([{l} x i8], [{l} x i8]* @{n}, i32 0, i32 0), i64 {l}, i1 false)\n"
        self.reg += 1
        self.buffer += f"%ptr{n} = alloca i8*\n"
        self.buffer += f"%{self.reg} = getelementptr inbounds [{l} x i8], [{l} x i8]* %{n}, i64 0, i64 0\n"
        self.reg += 1
        self.buffer += f"store i8* %{self.reg-1}, i8** %ptr{n}\n";    
        self.strr += 1
        
    def add_string(self, id1, l1:int, id2, l2:int):
        self.allocate_string(f"str{self.strr}", l1+l2)
        self.buffer += f"%ptrstr{self.strr} = alloca i8*\n"
        self.buffer += f"%{self.reg} = getelementptr inbounds [{l1+l2+1} x i8], [{l1+l2+1} x i8]* %str{self.strr}, i64 0, i64 0\n"
        self.reg +=1
        self.buffer += f"store i8* %{self.reg-1}, i8** %ptrstr{self.strr}\n" 
        self.buffer += f"%{self.reg} = load i8*, i8** %ptrstr{self.strr}\n"
        self.reg +=1  
        self.buffer += f"%{self.reg} = load i8*, i8** %ptrstr{self.strr-2}\n"
        self.reg +=1
        self.buffer += f"%{self.reg} = call i8* @strcpy(i8* %{self.reg-2}, i8* %{self.reg-1})\n"
        self.reg +=1
        self.buffer += f"%{self.reg} = load i8*, i8** %ptrstr{self.strr-1}\n"
        self.reg +=1
        self.buffer += f"%{self.reg} = call i8* @strcat(i8* %{self.reg-4}, i8* %{self.reg-1})\n"
        self.reg +=1
        self.strr += 1 
    
    def load_string(self, id):
        self.buffer += f"%{self.reg} = load i8*, i8** %{id}\n"
        self.reg += 1
        
    def show_array(self, id):
        array_length = self.stack[-1].length

        # Allocate memory for loop index
        self.buffer += f"%i = alloca i32\n"
        self.buffer += f"store i32 0, i32* %i\n"

        # Loop start
        loop_label = self.reg
        self.reg += 1
        self.buffer += f"br label %loop{loop_label}\n"
        self.buffer += f"loop{loop_label}:\n"

        # Load loop index
        self.buffer += f"%{self.reg} = load i32, i32* %i\n"
        loop_index = self.reg
        self.reg += 1

        # Check if loop index < array length
        self.buffer += f"%{self.reg} = icmp slt i32 %{loop_index}, {array_length}\n"
        self.reg += 1
        self.buffer += f"br i1 %{self.reg-1}, label %loop_body{loop_label}, label %loop_end{loop_label}\n"

        # Loop body
        self.buffer += f"loop_body{loop_label}:\n"
        self.buffer += f"%{self.reg} = getelementptr inbounds [{array_length} x i32], [{array_length} x i32]* %{id}, i32 0, i32 %{loop_index}\n"
        self.reg += 1
        self.buffer += f"%{self.reg} = load i32, i32* %{self.reg-1}\n"
        self.reg += 1
        self.buffer += f"%{self.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %{self.reg-1})\n"
        self.reg += 1

        # Increment loop index
        self.buffer += f"%{self.reg} = add i32 %{loop_index}, 1\n"
        self.reg += 1
        self.buffer += f"store i32 %{self.reg-1}, i32* %i\n"

        # Jump back to loop start
        self.buffer += f"br label %loop{loop_label}\n"

        # Loop end
        self.buffer += f"loop_end{loop_label}:\n"
        
        
    def print_specific_int_array_element(self, id, index):
        # Load the element at the specified index
        self.buffer += f"%{self.reg} = getelementptr inbounds [{index+1} x i32], [{index+1} x i32]* %{id}, i32 0, i32 {index}\n"
        self.reg += 1
        element_ptr = f"%{self.reg-1}"

        # Load the value of the element
        self.buffer += f"%{self.reg} = load i32, i32* {element_ptr}\n"
        self.reg += 1

        # Print the value of the element
        self.buffer += f"%{self.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %{self.reg-1})\n"
        self.reg += 1
        
    def print_int_element(self, value):
        self.buffer += f"%{self.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 {value})\n"
        self.reg += 1

    def scanf_string(self, id:str, l:int):
        self.allocate_string(f"str{self.strr}", l)
        self.buffer += f"%{id} = alloca i8*\n"
        self.buffer  += f"%{self.reg} = getelementptr inbounds [{l+1} x i8], [{l+1} x i8]* %str{self.strr}, i64 0, i64 0\n"
        self.reg += 1
        self.buffer  += f"store i8* %{self.reg-1} , i8** %{id} \n"; 
        self.strr += 1
        self.buffer  += f"%{self.reg}  = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @strs2, i32 0, i32 0), i8* %{self.reg-1} )\n"
        self.reg += 1
        
    def functionstart(self, id:str):
        self.buffer += self.buffer
        self.buffer = f"define i32 @{id}() nounwind {{ \n"
        self.main_tmp = self.reg
        self.reg = 1
        
    def functionend(self):
        self.buffer += f"ret i32 %{self.reg-1 }\n"; 
        self.buffer += "}\n"
        self.header_text += self.buffer
        self.buffer = ""
        self.reg = self.main_tmp
        
    def call(self, id: str):
        self.buffer += f"%{self.reg} = call i32 @{id}()\n"
        self.reg +=1
    
    def close_main(self):
        self.text += self.buffer    
        
    def ifstart(self):
        self.br += 1
        self.buffer += f"br i1 %{self.reg - 1}, label %true{self.br}, label %false{self.br}\n"
        self.buffer += f"true{self.br}:\n"
        self.brstack.append(self.br)
   
    def ifend(self):
        b = self.brstack.pop()
        self.buffer += f"br label %false{b}\n"
        self.buffer += f"false{b}:\n"
   
    def icmp(self, id:str, value: str):
        self.buffer += f"%{self.reg} = load i32, i32* {id}\n"
        self.reg += 1
        self.buffer += f"%{self.reg} = icmp eq i32 %{self.reg-1}, {value}\n"
        self.reg += 1
        
    tmp = 1
        
    def repeatstart(self, repetitions):
        self.declare_int(str(self.reg))
        counter = self.reg
        self.reg += 1
        self.assign_int(f"%{str(counter)}", "0")
        self.br += 1
        self.buffer += f"br label %cond{self.br}\n"
        self.buffer += f"cond{self.br}:\n"
        
        self.load_i32(f"%{str(counter)}")
        self.add_int_simple(f"%{self.reg-1}", "1")
        self.assign_int(f"%{str(counter)}", f"%{self.reg-1}")
        
        self.buffer += f"%{self.reg} = icmp slt i32 %{self.reg-2}, {repetitions}\n"
        self.reg += 1

        self.buffer += f"br i1 %{self.reg -1}, label %true{self.br}, label %false{self.br}\n"
        self.buffer += f"true{self.br}:\n"
        self.brstack.append(self.br)
   
    def repeatend(self):
        b = self.brstack.pop()
        self.buffer += f"br label %cond{b}\n"
        self.buffer += f"false{b}:\n"
        
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
        output += "@strs2 = constant [5 x i8] c\"%10s\\00\"\n"
        output += "@strs = constant [3 x i8] c\"%d\\00\"\n"
        output += "@.str = private unnamed_addr constant [3 x i8] c\"%d\\00\"\n"
        output += self.header_text
        output += "define i32 @main() nounwind{\n"
        output += self.text
        output += "ret i32 0 }\n"
        print(output)