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
%struct.Person = type { i32, i32, i32 }
%struct.Dog = type { i32 }
@x = global i32 0
define i32 @main() nounwind{
%person = alloca %struct.Person
%dog = alloca %struct.Dog
%1 = mul i32 13, 13
store i32 %1, i32* @x
%2 = load i32, i32* @x
%dog_age = getelementptr inbounds %struct.Person, ptr %dog, i32 0, i32 0
store i32 %2, ptr %dog_age
%3 = getelementptr inbounds %struct.Person, ptr %dog, i32 0, i32 0
%4 = load i32, ptr %3, align 4
%5 = call i32 (ptr, ...) @printf(ptr noundef @.str, i32 noundef %4)
ret i32 0 }

