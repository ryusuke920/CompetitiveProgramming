s = input()
ans = [1]*len(s)

for i in range(len(s) - 1):
    if s[i] == "R" and s[i+1] == "R":
        ans[i+2] += ans[i]
        ans[i] = 0

for i in range(len(s) - 1, 0, -1):
    if s[i] == "L" and s[i-1] == "L":
        ans[i-2] += ans[i]
        ans[i] = 0
    
print(*ans)