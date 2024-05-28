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
@a = global i32 0
define i32 @main() nounwind{
store i32 13, i32* @a
%1 = alloca i32
store i32 0, i32* %1
br label %cond1
cond1:
%2 = load i32, i32* %1
%3 = add i32 %2, 1
store i32 %3, i32* %1
%4 = icmp slt i32 %2, 3
br i1 %4, label %true1, label %false1
true1:
%5 = load i32, i32* @a
%6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %5)
br label %cond1
false1:
ret i32 0 }

