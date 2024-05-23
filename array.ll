declare i32 @printf(i8*, ...)
declare i32 @scanf(ptr noundef, ...) #1
declare i8* @strcpy(i8*, i8*)
declare i32 @atoi(i8*)
declare i8* @strcat(i8*, i8*)
declare void @llvm.memcpy.p0i8.p0i8.i64(i8* noalias nocapture writeonly, i8* noalias nocapture readonly, i64, i1 immarg)
@strpi = constant [4 x i8] c"%d\0A\00"
@strpd = constant [4 x i8] c"%f\0A\00"
@strps = constant [4 x i8] c"%s\0A\00"
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
%i = alloca i32
store i32 0, i32* %i
br label %loop5
loop5:
%6 = load i32, i32* %i
%7 = icmp slt i32 %6, 4
br i1 %7, label %loop_body5, label %loop_end5
loop_body5:
%8 = getelementptr inbounds [4 x i32], [4 x i32]* %a, i32 0, i32 %6
%9 = load i32, i32* %8
%10 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %9)
%11 = add i32 %6, 1
store i32 %11, i32* %i
br label %loop5
loop_end5:
%12 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 11)
ret i32 0 }

