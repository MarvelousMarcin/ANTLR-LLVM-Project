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
%a = alloca i32
store i32 5, i32* %a
%b = alloca i32
store i32 5, i32* %b
%y = alloca i32
store i32 13, i32* %y
%1 = load i32, i32* %a
%2 = load i32, i32* %b
%3 = mul i32 %1, %2
%4 = mul i32 %1, %2
%z = alloca i32
store i32 %4, i32* %z
%5 = load i32, i32* %z
%6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %5)
ret i32 0 }

