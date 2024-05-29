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
@a = global double 0.0
@b = global double 0.0
@z = global double 0.0
@p = global float 0.0
@d = global float 0.0
@c = global float 0.0
@x = global double 0.0
@k = global double 0.0
@y = global double 0.0
define i32 @main() nounwind{
store double 1.0, double* @a
store double 2.0, double* @b
store double 3.0, double* @z
store float 1.0, float* @p
store float 3.0, float* @d
%1 = load float, float* @p
%2 = load float, float* @d
%3 = fdiv float %1, %2
store float %3, float* @c
%4 = fpext float %3 to double
%5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %4)
%6 = load double, double* @z
%7 = load double, double* @b
%8 = load double, double* @a
%9 = fadd double %7, %8
%10 = fdiv double %6, %9
store double %10, double* @x
%11 = fdiv double 100.0, 3.0
store double %11, double* @k
%12 = load double, double* @x
%13 = fmul double %12, 100.0
%14 = fsub double %13, 3.0
%15 = fadd double %14, 9.0
store double %15, double* @y
%16 = load double, double* @k
%17 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %16)
ret i32 0 }

