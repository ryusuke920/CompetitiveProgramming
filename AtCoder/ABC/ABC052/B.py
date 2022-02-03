n = int(input())
s = str(input())
count = 0
ans = 0
for i in s:
    if i == "I":
        count += 1
    else:
        count -= 1
    ans = max(count,ans)
print(ans)