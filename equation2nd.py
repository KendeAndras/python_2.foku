import math


print("2.foku egyenlet")

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
x=int(input("x="))

res=(a*x**2+b*x+c)

dis=b**2-4*a*c

if dis<=0:
    print("nincs megoldas, a diszkriminans 0 nal kisebb")
    print("res=", res)
else:
    x1=(-b+math.sqrt((b**2-4*a*c)))/2*a
    x2=(-b-math.sqrt((b**2-4*a*c)))/2*a

    print("res=",res, "x1=", x1,"x2=", x2)

