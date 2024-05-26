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
store i32 1, i32* %x
%1 = load i32, i32* %x
%fun = alloca i32
store i32 %1, i32* %fun
%2 = load i32, i32* %fun
ret i32 %2
}
@z = global i32 0
@h = global i32 0
define i32 @main() nounwind{
%1 = call i32 @fun()
store i32 %1, i32* @z
%2 = load i32, i32* @z
%3 = icmp eq i32 %2, 1
br i1 %3, label %true1, label %false1
true1:
store i32 7, i32* @z
%4 = load i32, i32* @z
%5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %4)
%6 = load i32, i32* @z
%7 = icmp eq i32 %6, 7
br i1 %7, label %true2, label %false2
true2:
%8 = load i32, i32* @z
%9 = add i32 %8, 3
store i32 %9, i32* @h
%10 = load i32, i32* @h
%11 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %10)
br label %false2
false2:
br label %false1
false1:
ret i32 0 }

