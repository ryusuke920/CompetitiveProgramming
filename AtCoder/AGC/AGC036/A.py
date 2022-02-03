S = int(input())
x = 10**9
# S + x3 = y3 * 10**9
x3 = (x-S)%x
y3 = (S+x3)//x
print(0,0,x,1,x3,y3)