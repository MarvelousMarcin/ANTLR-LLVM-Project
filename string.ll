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
@str2 = constant [13 x i8] c"ala ma kota \00"
@str3 = constant [9 x i8] c" fajnego\00"
@str5 = constant [22 x i8] c" jest to text testowy\00"
define i32 @main() nounwind{
%str1 = alloca [510 x i8]
%b = alloca i8*
%1 = getelementptr inbounds [17 x i8], [17 x i8]* %str1, i64 0, i64 0
store i8* %1 , i8** %b 
%2  = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @strs2, i32 0, i32 0), i8* %1 )
%3 = load i8*, i8** %b
%4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strps, i32 0, i32 0), i8* %3)
%str2 = alloca [390 x i8]
%5 = bitcast [13 x i8]* %str2 to i8*
call void @llvm.memcpy.p0i8.p0i8.i64(i8* align 1 %5, i8* align 1 getelementptr inbounds ([13 x i8], [13 x i8]* @str2, i32 0, i32 0), i64 13, i1 false)
%ptrstr2 = alloca i8*
%6 = getelementptr inbounds [13 x i8], [13 x i8]* %str2, i64 0, i64 0
store i8* %6, i8** %ptrstr2
%str3 = alloca [270 x i8]
%7 = bitcast [9 x i8]* %str3 to i8*
call void @llvm.memcpy.p0i8.p0i8.i64(i8* align 1 %7, i8* align 1 getelementptr inbounds ([9 x i8], [9 x i8]* @str3, i32 0, i32 0), i64 9, i1 false)
%ptrstr3 = alloca i8*
%8 = getelementptr inbounds [9 x i8], [9 x i8]* %str3, i64 0, i64 0
store i8* %8, i8** %ptrstr3
%str4 = alloca [630 x i8]
%ptrstr4 = alloca i8*
%9 = getelementptr inbounds [21 x i8], [21 x i8]* %str4, i64 0, i64 0
store i8* %9, i8** %ptrstr4
%10 = load i8*, i8** %ptrstr4
%11 = load i8*, i8** %ptrstr2
%12 = call i8* @strcpy(i8* %10, i8* %11)
%13 = load i8*, i8** %ptrstr3
%14 = call i8* @strcat(i8* %10, i8* %13)
%a = alloca i8*
store i8* %14, i8** %a
%15 = load i8*, i8** %a
%str5 = alloca [660 x i8]
%16 = bitcast [22 x i8]* %str5 to i8*
call void @llvm.memcpy.p0i8.p0i8.i64(i8* align 1 %16, i8* align 1 getelementptr inbounds ([22 x i8], [22 x i8]* @str5, i32 0, i32 0), i64 22, i1 false)
%ptrstr5 = alloca i8*
%17 = getelementptr inbounds [22 x i8], [22 x i8]* %str5, i64 0, i64 0
store i8* %17, i8** %ptrstr5
%str6 = alloca [660 x i8]
%ptrstr6 = alloca i8*
%18 = getelementptr inbounds [22 x i8], [22 x i8]* %str6, i64 0, i64 0
store i8* %18, i8** %ptrstr6
%19 = load i8*, i8** %ptrstr6
%20 = load i8*, i8** %ptrstr4
%21 = call i8* @strcpy(i8* %19, i8* %20)
%22 = load i8*, i8** %ptrstr5
%23 = call i8* @strcat(i8* %19, i8* %22)
%h = alloca i8*
store i8* %23, i8** %h
%24 = load i8*, i8** %h
%25 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strps, i32 0, i32 0), i8* %24)
ret i32 0 }

