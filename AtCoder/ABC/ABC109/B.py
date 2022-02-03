n = int(input())
w = [str(input()) for i in range(n)]
used = []
count = 0
for i in range(n-1):
    if((w[i] not in used) and (w[i][-1] == w[i+1][0])):
        count += 1
        used.append(w[i])
if count == n-1 and w[-1] not in used:
    print("Yes")
else:
    print("No")