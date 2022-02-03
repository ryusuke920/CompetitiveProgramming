def area(a: int, b: int) -> int:
    return 4 * a * b + 3 * a + 3 * b

n = int(input())
s = list(map(int, input().split()))

ans = 0
for i in s:
    bool = False
    for a in range(1, 251):
        for b in range(1, 251):
            if area(a, b) == i:
                bool = True
    
    if bool:
        ans += 1

print(n - ans)