n, k = map(int,input().split())
t = list(input())
for i in range(k - 1, n):
    if t[i] == "j": t[i] = "J"
    elif t[i] == "o": t[i] = "O"
    elif t[i] == "i": t[i] = "I"
    elif t[i] == "J": t[i] = "j"
    elif t[i] == "O": t[i] = "o"
    elif t[i] == "I": t[i] = "i"
print(*t, sep="")