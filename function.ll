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
store i32 9, i32* %x
%1 = load i32, i32* %x
%fun = alloca i32
store i32 %1, i32* %fun
%2 = load i32, i32* %fun
ret i32 %2
}
@x = global i32 0
@ala = global i32 0
define i32 @main() nounwind{
store i32 13, i32* @x
%1 = call i32 @fun()
store i32 %1, i32* @ala
%2 = load i32, i32* @x
%3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %2)
%4 = load i32, i32* @ala
%5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %4)
ret i32 0 }

