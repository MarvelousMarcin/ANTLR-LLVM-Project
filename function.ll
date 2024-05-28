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
define i32 @fun() nounwind { 
%x = alloca i32
store i32 3, i32* %x
%1 = add i32 3, 2
%y = alloca i32
store i32 %1, i32* %y
%2 = alloca i32
store i32 0, i32* %2
br label %cond1
cond1:
%3 = load i32, i32* %2
%4 = add i32 %3, 1
store i32 %4, i32* %2
%5 = icmp slt i32 %3, 3
br i1 %5, label %true1, label %false1
true1:
%6 = load i32, i32* %x
%7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %6)
br label %cond1
false1:
%8 = load i32, i32* %y
%9 = icmp eq i32 %8, 5
br i1 %9, label %true2, label %false2
true2:
%10 = load i32, i32* %x
%11 = add i32 %10, 3
store i32 %11, i32* %x
%12 = load i32, i32* %x
%13 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %12)
br label %false2
false2:
%14 = load i32, i32* %y
%fun = alloca i32
store i32 %14, i32* %fun
%15 = load i32, i32* %fun
ret i32 %15
}
@output = global i32 0
define i32 @main() nounwind{
%1 = call i32 @fun()
store i32 %1, i32* @output
%2 = load i32, i32* @output
%3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %2)
ret i32 0 }

