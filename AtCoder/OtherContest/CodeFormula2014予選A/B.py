a,b = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
ans = ["x"]*10
for i in range(a):
    if p[i] == 0:
        ans[9] = "."
    else:
        ans[p[i]-1] = "."
for j in range(b):
    if q[j] == 0:
        ans[9] = "o"
    else:
        ans[q[j]-1] = "o"
print(ans[6],ans[7],ans[8],ans[9])
print("",ans[3],ans[4],ans[5])
print(" ",ans[1],ans[2])
print("  ",ans[0])