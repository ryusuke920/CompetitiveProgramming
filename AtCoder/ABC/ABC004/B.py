ans = ""
for i in range(4):
    c = list(map(str,input().split()))
    ans += " ".join(c)
    ans += " "
ans = ans[::-1]
ans = ans[1:]
for i in range(4):
    print(ans[8*i:8*(i+1)-1])