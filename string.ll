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
@marcin = global i32 0
@kristi = global i32 0
define i32 @main() nounwind{
store i32 69, i32* @marcin
store i32 69, i32* @kristi
%1 = load i32, i32* @marcin
%2 = icmp eq i32 %1, 69
br i1 %2, label %true1, label %false1
true1:
%3 = alloca i32
store i32 0, i32* %3
br label %cond2
cond2:
%4 = load i32, i32* %3
%5 = add i32 %4, 1
store i32 %5, i32* %3
%6 = icmp slt i32 %4, 3
br i1 %6, label %true2, label %false2
true2:
%7 = load i32, i32* @kristi
%8 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %7)
br label %cond2
false2:
%9 = load i32, i32* @marcin
br label %false1
false1:
ret i32 0 }

