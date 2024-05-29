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
@a = global double 0.0
@b = global double 0.0
@z = global double 0.0
@x = global double 0.0
@k = global double 0.0
@y = global double 0.0
define i32 @main() nounwind{
store double 1.0, double* @a
store double 2.0, double* @b
store double 3.0, double* @z
%1 = load double, double* @z
%2 = load double, double* @b
%3 = load double, double* @a
%4 = fadd double %2, %3
%5 = fdiv double %1, %4
store double %5, double* @x
%6 = fdiv double 100.0, 3.0
store double %6, double* @k
%7 = load double, double* @x
%8 = fmul double %7, 100.0
%9 = fsub double %8, 3.0
%10 = fadd double %9, 9.0
store double %10, double* @y
%11 = load double, double* @x
%12 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %11)
ret i32 0 }

