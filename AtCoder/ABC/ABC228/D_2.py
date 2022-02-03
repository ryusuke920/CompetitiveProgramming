s = input()
k = int(input())

l = 0
ans = 0
c_cnt = 0
cnt = 0
for r in range(len(s)):
    if s[r] == 'X':
        cnt += 1
    elif s[r] == '.':
        cnt += 1
        c_cnt += 1
    
    if c_cnt > k:
        while True:
            cnt -= 1
            if s[l] == '.':
                c_cnt -= 1
            l += 1
            if c_cnt <= k: break
    
    ans = max(ans, cnt)

print(ans)