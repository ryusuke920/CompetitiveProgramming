ans = []
while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int,input().split()))
    ans.append(max(a))

for i in range(len(ans)):
    print(ans[i])