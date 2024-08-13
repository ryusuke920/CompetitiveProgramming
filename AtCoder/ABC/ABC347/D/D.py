def main() -> None:
    a, b, C = map(int, input().split())
    bit_ = bin(C)[2:].count('1')
    
    is_check = False
    cnt = 0
    min_ = min(a, b)
    for i in range(min_ + 1):
        if (a + b - 2*i) == bit_:
            is_check = True
            cnt = i
            # cnt = i + 1
            break

    if not is_check:
        exit(print(-1))

    X, Y = 0, 0
    ans = a - cnt
    p, q = a - cnt, b - cnt
    for i in range(64):
        if ((C >> i) & 1):
            if p > 0:
                X += (1 << i)
                p -= 1
            elif q > 0:
                Y += (1 << i)
                q -= 1
        else:
            if cnt:
                X += (1 << i)
                Y += (1 << i)
                cnt -= 1

    if not (0 <= X < 2**60): exit(print(-1))
    if not (0 <= Y < 2**60): exit(print(-1))
    if bin(X)[2:].count("1") != a: exit(print(-1))
    if bin(Y)[2:].count("1") != b: exit(print(-1))
    if X ^ Y != C: exit(print(-1))

    print(X, Y)



if __name__ == "__main__":
    main()