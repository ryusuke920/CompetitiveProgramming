s = list(input())
ans = cnt = i = num = 0
while i < len(s):
    if s[i] == "2" and cnt == 0:
        cnt = 1
    elif cnt == 1:
        if s[i] == "5":
            cnt = 2
            num += 1
        elif s[i] == "2":
            cnt = 1
        else:
            num = cnt = 0
    elif cnt == 2:
        if s[i] == "2":
            cnt = 3
        else:
            ans += num*(num + 1)//2
            num = cnt = 0
    elif cnt == 3:
        if s[i] == "5":
            num += 1
            cnt = 2
        elif s[i] == "2":
            ans += num*(num + 1)//2
            num = 0
            cnt = 1
        else:
            ans += num*(num + 1)//2
            num = cnt = 0
    else:
        ans += num*(num + 1)//2
        num = cnt = 0
    i += 1
print(ans + num*(num + 1)//2)