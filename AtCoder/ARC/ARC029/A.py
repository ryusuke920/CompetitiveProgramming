n = int(input())
t = [int(input()) for _ in range(n)]
t.sort()
if n == 1:
    print(t[0])
elif n == 2:
    print(max(t[0],t[1]))
elif n == 3:
    print(min(max(t[0]+t[1],t[2]), max(t[0]+t[2],t[1])) )
else:
    print(min(max(t[0]+t[1],t[2]+t[3]), max(t[0]+t[2],t[1]+t[3]), max(t[0]+t[3],t[1]+t[2]), max(t[0]+t[1]+t[2],t[3])) )