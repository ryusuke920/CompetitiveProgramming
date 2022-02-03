n, k = map(int,input().split())
s = input()
word = {"R" : 1, "P" : 2, "S" : 3}
ans = {1 : "R", 2 : "P", 3 : "S"}
num = [word[i] for i in s]

def winner(x, y):
    if x == y:
        return x
    elif (x, y) == (2, 1) or (x, y) == (1, 2):
        return 2
    elif (x, y) == (1, 3) or (x, y) == (3, 1):
        return 1
    elif (x, y) == (2, 3) or (x, y) == (3, 2):
        return 3

for i in range(k):
    t = 2 * num
    for j in range(n):
        num[j] = winner(t[2 * j], t[2 * j + 1])

print(ans[num[0]])