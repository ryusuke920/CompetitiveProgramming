def rle(S: str) -> list:
    tmp, cnt, ans = S[0], 1, []
    for i in range(1, len(S)):
        if tmp == S[i]:
            cnt += 1
        else:
            ans.append(cnt)
            tmp, cnt = S[i], 1
    ans.append(cnt)

    return ans

input()
print(sum([i * (i - 1) // 2 for i in rle(input())]))