n = int(input())
s = list(input())
black = s.count("#")
front_black = 0
ans = n - black # 初期がこの状態で１つずつみぎにシフトしていく
for i in range(n):
    if s[i] == "#":
        front_black += 1
    ans = min(ans, front_black + (n - i - 1 - (black - front_black)))
print(ans)