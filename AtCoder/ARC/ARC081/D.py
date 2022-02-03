n = int(input())
s1 = input()
s2 = input()
mod = 10 ** 9 + 7
i = 0
while True:
    if i >= len(s1):
        break
    if i == 0:
        if s1[i] == s2[i]:
            ans = 3
            i += 1
            check = 1 # 縦
        else:
            ans = 6
            i += 2
            check = 2 # 横
    else: # i != 1
        if check == 1:
            if s1[i] == s2[i]: # 縦で縦
                ans *= 2
                check = 1
                i += 1
            else: # 縦で横
                ans *= 2
                check = 2
                i += 2
        else: # check == 2:
            if s1[i] == s2[i]: # 横で縦
                ans *= 1
                check = 1
                i += 1 
            else: # 横で横
                ans *= 3
                check = 2
                i += 2
    ans %= mod
print(ans)