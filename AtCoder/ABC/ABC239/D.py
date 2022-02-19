def PrimaryCheck(x: int) -> bool:
    if x == 1: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

a, b, c, d = map(int, input().split())
cnt = 0
for i in range(a, b + 1):
    bool = False
    for j in range(c, d + 1):
        if PrimaryCheck(i + j):
            bool = True
            break
    
    if bool:
        cnt += 1

if cnt == b - a + 1:
    print('Aoki')
else:
    print('Takahashi')