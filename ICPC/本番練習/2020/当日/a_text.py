ans = []
while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(str,input().split()))
    ch = ["2","0","2","0"]
    num = 0
    for i in range(n-3):
        if a[i:i+4] == ch:
            num += 1
    ans.append(num)
for i in range(len(ans)):
    print(ans[i])