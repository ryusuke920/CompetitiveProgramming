n = int(input())
a = list(map(int,input().split()))
num = [i + 1 for i in range(n)]
a.sort()
num.sort()
#print(a,num)
if a == num:
    print("Yes")
else:
    print("No")
ans = cnt = 0