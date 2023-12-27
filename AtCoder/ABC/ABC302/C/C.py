from itertools import permutations

def main() -> None:
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]

    for p in permutations(range(n)):
        check = True
        for i in range(n - 1):
            cnt = 0
            for j in range(m):
                if s[p[i]][j] != s[p[i + 1]][j]:
                    cnt += 1
            if cnt != 1:
                check = False
                break
        if check:
            exit(print("Yes"))
    
    print("No")


if __name__ == "__main__":
    main()