import sys
input = sys.stdin.readline

def main() -> None:
    N = int(input())
    C = []
    A = []
    for _ in range(N):
        C.append(int(input()))
        A.append(list(map(int, input().split())))
    X = int(input())
    ans = []
    for i in range(N):
        check = False
        for j in range(C[i]):
            if A[i][j] == X:
                check = True
                break
        
        if check:
            ans.append((C[i], i + 1))
    
    ans.sort(key=lambda x: x[0])
    p = 0
    t = []
    for i in range(len(ans)):
        if ans[i][0] == ans[0][0]:
            p += 1
            t.append(ans[i][1])
    print(p)
    if p > 0:
        print(*t)


if __name__ == "__main__":
    main()