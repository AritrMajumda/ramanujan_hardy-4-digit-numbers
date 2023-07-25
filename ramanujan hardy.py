import math
l=float(input("enter a four digit number: "))
s1=0
s2=0
c=0
s=0
l1= math.pow(l,1/3)
l2=int(l1)
for i in range(1,l2):
    s1=i
    for j in range (1,l2):
        s2=j
        s=(s1*s1*s1)+(s2*s2*s2)
        if(s==l):
            c=c+1
        else:
            continue
if(c==2):
    print("the given number is a ramanujan-hardy number")
else:
    print("the given number is not a ramanujan-hardy number")



        