x = input()
ans = 0
for i in range(len(x)):
    ans = max(ans, int(x[i]))
print(ans)