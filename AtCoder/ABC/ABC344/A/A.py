s = list(input())
ans = []
cnt = 0
for i in s:
    if i == '|':
        cnt += 1
    else:
        if cnt == 0 or cnt >= 2:
            ans.append(i)

print("".join(ans))