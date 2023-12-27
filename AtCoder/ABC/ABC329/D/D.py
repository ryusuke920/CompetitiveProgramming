import sys
input = sys.stdin.readline
from heapq import heapify, heappop, heappush

def main() -> None:
    n, m = map(int, input().split())
    a = list(map(lambda x: int(x) - 1, input().split()))

    num = [0] * n
    num[a[0]] = 1 
    max_ = 1
    ind = a[0]
    print(ind + 1)
    q = [a[0]]
    heapify(q)
    for i in range(1, m):
        num[a[i]] += 1
        if num[a[i]] == max_:
            heappush(q, a[i])
            p = heappop(q)
            ind = p
            heappush(q, p)
        elif num[a[i]] > max_:
            max_ = num[a[i]]
            q = [a[i]]
            heapify(q)
            ind = a[i]

        print(ind + 1)


if __name__ == "__main__":
    main()