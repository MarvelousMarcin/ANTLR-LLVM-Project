declare i32 @printf(i8*, ...)
declare i32 @scanf(ptr noundef, ...) #1
declare i8* @strcpy(i8*, i8*)
declare i32 @atoi(i8*)
declare i8* @strcat(i8*, i8*)
declare void @llvm.memcpy.p0i8.p0i8.i64(i8* noalias nocapture writeonly, i8* noalias nocapture readonly, i64, i1 immarg)
@strpi = constant [4 x i8] c"%d\0A\00"
@strpd = constant [4 x i8] c"%f\0A\00"
@strps = constant [4 x i8] c"%s\0A\00"
@strs2 = constant [5 x i8] c"%10s\00"
@strs = constant [3 x i8] c"%d\00"
@.str = private unnamed_addr constant [3 x i8] c"%d\00"
define i32 @pow() nounwind { 
%x = alloca i32
store i32 100, i32* %x
%1 = load i32, i32* %x
%2 = load i32, i32* %x
%3 = mul i32 %1, %2
%pow = alloca i32
store i32 %3, i32* %pow
%4 = load i32, i32* %pow
ret i32 %4
}
define i32 @fun() nounwind { 
%x = alloca i32
store i32 3, i32* %x
%1 = add i32 3, 2
%y = alloca i32
store i32 %1, i32* %y
%2 = load i32, i32* %y
%3 = alloca i32
store i32 0, i32* %3
br label %cond1
cond1:
%4 = load i32, i32* %3
%5 = add i32 %4, 1
store i32 %5, i32* %3
%6 = icmp slt i32 %4, %2
br i1 %6, label %true1, label %false1
true1:
%7 = load i32, i32* %x
%8 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %7)
br label %cond1
false1:
%9 = call i32 @pow()
%z = alloca i32
store i32 %9, i32* %z
%10 = load i32, i32* %y
%11 = icmp eq i32 %10, 5
br i1 %11, label %true2, label %false2
true2:
%12 = load i32, i32* %x
%13 = add i32 %12, 3
store i32 %13, i32* %x
%14 = load i32, i32* %x
%15 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %14)
%16 = load i32, i32* %z
%17 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %16)
br label %false2
false2:
%18 = load i32, i32* %y
%fun = alloca i32
store i32 %18, i32* %fun
%19 = load i32, i32* %fun
ret i32 %19
}
@x = global i32 0
@output = global i32 0
define i32 @main() nounwind{
store i32 10, i32* @x
%1 = call i32 @fun()
store i32 %1, i32* @output
%2 = load i32, i32* @output
%3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %2)
%4 = load i32, i32* @x
%5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %4)
ret i32 0 }

