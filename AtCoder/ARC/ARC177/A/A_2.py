from typing import List
import heapq

A, B, C, D, E, F = 0, 0, 0, 0, 0, 0
N = 0
X: List[int] = []

def f(PQ, val, cnt):
    for _ in range(cnt):
        tmp = PQ[0]
        if tmp < val:
            break
        heapq.heappop(PQ)
        tmp -= val
        heapq.heappush(PQ, -tmp)

def solve():
    global A, B, C, D, E, F, N, X
    PQ = []
    for i in range(N):
        heapq.heappush(PQ, -X[i])
    f(PQ, 500, F)
    f(PQ, 100, E)
    f(PQ, 50, D)
    f(PQ, 10, C)
    f(PQ, 5, B)
    f(PQ, 1, A)
    if -PQ[0] == 0:
        print("Yes")
    else:
        print("No")

def main():
    global A, B, C, D, E, F, N, X
    A, B, C, D, E, F = map(int, input().split())
    N = int(input())
    X = list(map(int, input().split()))
    solve()

if __name__ == "__main__":
    main()