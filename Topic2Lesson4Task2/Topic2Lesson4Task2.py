﻿x = int(input("Введите пятизначное число "))
x1 = x%10//1
x10 = x%100//10
x100 = x%1000//100
x1000 = x%10000//1000
x10000 = x%100000//10000
dx =x10**x1*x100//(x10000-x1000)
print(x10,"^",x1,"*",x100,"/(",x10000,"-",x1000,") =",dx)
