while True:
    n = input()
    if n == "0":
        exit()
    ans = 0
    for i in range(len(n)):
        ans += int(n[i])
    print(ans)