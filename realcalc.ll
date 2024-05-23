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
%a = alloca double
store double 1.0, double* %a
%b = alloca double
store double 2.0, double* %b
%z = alloca double
store double 3.0, double* %z
%1 = load double, double* %z
%2 = load double, double* %b
%3 = fdiv double %1, %2
%4 = load double, double* %a
%5 = fadd double %3, %4
%answer = alloca double
store double %5, double* %answer
%6 = load double, double* %answer
%7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %6)
ret i32 0 }

