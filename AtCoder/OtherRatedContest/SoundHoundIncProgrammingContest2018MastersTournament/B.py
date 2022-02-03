s = str(input())
n = int(input())
if len(s)%n == 0:
    cnt = len(s)//n
else:
    cnt = len(s)//n + 1
ans = []
for i in range(cnt):
    ans.append(s[i*n])
print(*ans, sep = "")