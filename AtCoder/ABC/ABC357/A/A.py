from random import randint
cnt = 0
n = 10**5
for _ in range(n):
    a = randint(1, 6)
    b = randint(1, 6)
    if a + b >= 7 and a == 4:
        cnt += 1
print(cnt)
print(cnt/n*100)