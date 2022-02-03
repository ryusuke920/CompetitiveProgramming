n = int(input())
a = str(input())
ans = [0]*4
for i in a:
    ans[int(i)-1] += 1
print(max(ans),min(ans))