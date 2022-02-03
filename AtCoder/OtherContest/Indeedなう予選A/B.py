from collections import Counter
ch = "indeednow"
x = Counter(ch)
n = int(input())
for i in range(n):
    s = input()
    y = Counter(s)
    if x == y:
        print("YES")
    else:
        print("NO")