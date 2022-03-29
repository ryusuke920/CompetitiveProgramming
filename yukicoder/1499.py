for _ in range(int(input())):
    s = input()
    for i in reversed(range(1, 101)):
        if str(i) in s:
            print(f'Hitsuji ga {i + 1} hiki')
            break