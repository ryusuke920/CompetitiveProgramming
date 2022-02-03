n = int(input())
for i in range(1,n+1):
    ans = []
    if i%2 == 0:
        ans.append("a")
    if i%3 == 0:
        ans.append("b")
    if i%4 == 0:
        ans.append("c")
    if i%5 == 0:
        ans.append("d")
    if i%6 == 0:
        ans.append("e")
    if len(ans) == 0:
        print(i)
    else:
        print(*ans, sep = "")
    ans = []