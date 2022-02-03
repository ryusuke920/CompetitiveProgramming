import math
A,B,C,D=map(int,input().split())
counta = math.ceil(A/D)
countb = math.ceil(C/B)

if counta>=countb:
    print("Yes")
else :
    print("No")