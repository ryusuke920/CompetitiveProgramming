def main() -> None:

    h1, h2, h3, w1, w2, w3 = map(int, input().split())

    ans = 0
    for a11 in range(1, 31):
        for a12 in range(1, 31):
            for a21 in range(1, 31):
                for a22 in range(1, 31):
                    a13 = w1 - a11 - a12
                    a23 = w2 - a21 - a22
                    a31 = h1 - a11 - a21
                    a32 = h2 - a12 - a22
                    a33 = h3 - a13 - a23
                    
                    cnt = [a11, a12, a13, a21, a22, a23, a31, a32, a33]
                    check = True

                    for i in cnt:
                        if not (1 <= i <= 30):
                            check = False
                            break

                    if check:
                        if a11 + a12 + a13 != w1:
                            continue
                        if a21 + a22 + a23 != w2:
                            continue
                        if a31 + a32 + a33 != w3:
                            continue
                        if a11 + a21 + a31 != h1:
                            continue
                        if a12 + a22 + a32 != h2:
                            continue
                        if a13 + a23 + a33 != h3:
                            continue
                        ans += 1
    print(ans)


if __name__ == '__main__':
    main()