n = int(input())
ans = 0
x = 1000 - n
while x > 0:
    if x >= 500:
        x -= 500
    elif x >= 100:
        x -= 100
    elif x >= 50:
        x -= 50
    elif x >= 10:
        x -= 10
    elif x >= 5:
        x -= 5
    elif x >= 1:
        x -= 1
    ans += 1
print(ans)