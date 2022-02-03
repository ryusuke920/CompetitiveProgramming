n = int(input())
ans = a = b = ab = 0
for i in range(n):
    s = input()
    for i in range(len(s)-1):
        if s[i] == "A" and s[i+1] == "B":
            ans += 1
    if s[0] == "B" and s[-1] == "A":
        ab += 1
    elif s[0] == "B":
        b += 1
    elif s[-1] == "A":
        a += 1
if ab == 0:
    print(ans + min(a,b))
else:
    if a+b > 0:
        print(ans + ab + min(a,b))
    else: # a+b = 0
        print(ans + ab-1)