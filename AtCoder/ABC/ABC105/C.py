n = int(input())
ans = []
if n % 2 == 1:
    ans.append(1)
else:
    ans.append(0)
diff = n - sum(ans) # そこまでの差
i = 1
while True:
    if diff == 0:
        break
    if diff % 2 ** (i + 1) == 2 ** i:
        ans.append(1)
        diff += (-1) ** i * 2 ** i
    else:
        ans.append(0)
    i += 1
print(ans)
"""
s1 -> 1のとき 
s1 -> 0のとき
"""