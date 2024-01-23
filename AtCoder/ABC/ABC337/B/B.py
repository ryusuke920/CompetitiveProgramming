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

s = input()
rle = RLE(s)
ans = ""
for i, j in rle:
    ans += i

print(ans)
t = ["ABC", "AB", "BC", "AC", "A", "B", "C"]
if ans in t:
    print("Yes")
else:
    print("No")