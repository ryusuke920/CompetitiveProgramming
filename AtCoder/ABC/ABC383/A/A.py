import sys
input = sys.stdin.readline

def main() -> None:
    N = int(input())
    T, V = [0]*N, [0]*N
    for i in range(N):
        T[i], V[i] = map(int, input().split())
    
    ans = V[0]
    for i in range(1, N):
        ans -= T[i] - T[i - 1]
        ans = max(ans, 0)
        ans += V[i]
    print(ans)


if __name__ == "__main__":
    main()