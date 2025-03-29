import sys
input = sys.stdin.readline

def main() -> None:
    N = int(input())
    P = list(map(int, input().split()))
    score = []
    for i in range(N):
        score.append((P[i], i))
    score.sort(key=lambda x: x[0], reverse=True)
    rank = 1
    i = 0
    ans = [-1]*N
    while i < N:
        num = P.count(score[i][0])
        for j in range(num):
            ans[score[i + j][1]] = rank
        rank += num
        i += num

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()