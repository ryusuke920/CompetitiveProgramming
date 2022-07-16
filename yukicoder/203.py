def RLE(S: str) -> list:
    tmp, cnt, ans = S[0], 1, []
    for i in range(1, len(S)):
        if tmp == S[i]:
            cnt += 1
        else:
            ans.append((tmp, cnt))
            tmp = S[i]
            cnt = 1

    ans.append((tmp, cnt))

    return ans

c1 = input()
c2 = input()
c = c1 + c2
l = RLE(c)

ans = 0
for k, v in l:
    if k == 'o':
        ans = max(ans, v)

print(ans)