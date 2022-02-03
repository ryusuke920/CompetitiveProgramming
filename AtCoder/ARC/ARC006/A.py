e = list(map(int,input().split()))
b = int(input())
l = list(map(int,input().split()))
ans = 0
bonus = 0
if b in l:
    bonus += 1
for i in range(6):
    for j in range(6):
        if e[i] == l[j]:
            ans += 1
            
if ans == 6:
    print(1)
elif ans + bonus == 6:
    print(2)
elif ans == 5:
    print(3)
elif ans == 4:
    print(4)
elif ans == 3:
    print(5)
else:
    print(0)