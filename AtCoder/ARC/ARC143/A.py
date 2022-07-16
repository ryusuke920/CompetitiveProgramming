a, b, c = sorted(list(map(int, input().split())), reverse=True)
print(-1) if a > b + c else print(a)