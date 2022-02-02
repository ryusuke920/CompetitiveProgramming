n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
x = sum(a)/n
y = sum(b)/n
if x > y:
    print("A")
elif x < y:
    print("B")
else:
    print("same")