n = int(input())
s = [input() for _ in range(n)]
x, y = set(), set() # !がついてるやつ, ついてないやつ
for i in s:
    if i[0] == "!":
        x.add(i[1:])
    else:
        y.add(i)

ans = x & y
if ans:
    print(ans.pop())
else:
    print("satisfiable")