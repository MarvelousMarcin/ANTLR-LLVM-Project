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
define i32 @main() nounwind{
%a = alloca [4 x i32]
%1 = getelementptr inbounds [1 x i32], [1 x i32]* %a, i32 0, i32 0
store i32 11, i32* %1
%2 = getelementptr inbounds [2 x i32], [2 x i32]* %a, i32 0, i32 1
store i32 32, i32* %2
%3 = getelementptr inbounds [3 x i32], [3 x i32]* %a, i32 0, i32 2
store i32 33, i32* %3
%4 = getelementptr inbounds [4 x i32], [4 x i32]* %a, i32 0, i32 3
store i32 22, i32* %4
%b = alloca [4 x i32]
%5 = getelementptr inbounds [1 x i32], [1 x i32]* %b, i32 0, i32 0
store i32 200, i32* %5
%6 = getelementptr inbounds [2 x i32], [2 x i32]* %b, i32 0, i32 1
store i32 100, i32* %6
%7 = getelementptr inbounds [3 x i32], [3 x i32]* %b, i32 0, i32 2
store i32 300, i32* %7
%8 = getelementptr inbounds [4 x i32], [4 x i32]* %b, i32 0, i32 3
store i32 500, i32* %8
%i = alloca i32
store i32 0, i32* %i
br label %loop9
loop9:
%10 = load i32, i32* %i
%11 = icmp slt i32 %10, 4
br i1 %11, label %loop_body9, label %loop_end9
loop_body9:
%12 = getelementptr inbounds [4 x i32], [4 x i32]* %b, i32 0, i32 %10
%13 = load i32, i32* %12
%14 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %13)
%15 = add i32 %10, 1
store i32 %15, i32* %i
br label %loop9
loop_end9:
%16 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 200)
ret i32 0 }

