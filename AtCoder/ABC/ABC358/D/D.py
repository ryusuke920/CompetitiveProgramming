'''
oj（online-judge-tools）の使い方について

1. テストケースをダウンロード
2. サンプルが合っているかジャッジする
3. 提出する

oj d https://atcoder.jp/contests/abc358/tasks/abc358_d
oj t -c "python3 D.py"
oj s https://atcoder.jp/contests/abc358/tasks/abc358_d D.py --guess-python-interpreter pypy

※test/ が既に作成されている場合は下記コマンドで test/ を削除する
rm -rf test/
'''

import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

# 99.99% tatyam さんが公開されている SortedMultiset を使用しています
# 一部自分用に変換しています

# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py

# https://qiita.com/tatyam/items/492c70ac4c955c055602

'''
SortedMultisetの使用例

ABC253-C - Max - Min Query https://atcoder.jp/contests/abc253/tasks/abc253_c
'''


from math import ceil, sqrt
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
T = TypeVar('T')

class SortedMultiset(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170


    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None:
            a = list(self)

        size = self.size = len(a)
        bucket_size = int(ceil(sqrt(size / self.BUCKET_RATIO)))
        self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]
    

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
        a = list(a)
        if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
            a = sorted(a)
        self._build(a)


    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i:
                yield j


    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i):
                yield j
    

    def __len__(self) -> int:
        return self.size
    

    def __repr__(self) -> str:
        return "SortedMultiset" + str(self.a)
    
    
    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"


    def _find_bucket(self, x: T) -> List[T]:
        "Find the bucket which should contain x. self must not be empty."
        for a in self.a:
            if x <= a[-1]:
                return a

        return a


    def __contains__(self, x: T) -> bool:
        if self.size == 0:
            return False

        a = self._find_bucket(x)
        i = bisect_left(a, x)
        return i != len(a) and a[i] == x


    def count(self, x: T) -> int:
        "Count the number of x."
        return self.index_right(x) - self.index(x)


    def add(self, x: T) -> None:
        "Add an element. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return

        a = self._find_bucket(x)
        insort(a, x)
        self.size += 1

        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()


    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0:
            return False

        a = self._find_bucket(x)
        i = bisect_left(a, x)

        if i == len(a) or a[i] != x:
            return False

        a.pop(i)
        self.size -= 1

        if len(a) == 0:
            self._build()

        return True


    def lt(self, x: T) -> Union[T, None]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]


    def le(self, x: T) -> Union[T, None]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]


    def gt(self, x: T) -> Union[T, None]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    
    def ge(self, x: T) -> Union[T, None]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]
    

    def __getitem__(self, x: int) -> T:
        "Return the x-th element, or IndexError if it doesn't exist."
        if x < 0:
            x += self.size

        if x < 0:
            raise IndexError

        for a in self.a:
            if x < len(a): return a[x]
            x -= len(a)
            
        raise IndexError


    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)

        return ans


    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)

        return ans

def main() -> None:
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    SM = SortedMultiset(A)

    ans = 0
    for i in range(M):
        t = SM.ge(B[i])
        if t == None:
            exit(print(-1))
        else:
            ans += t
            SM.discard(t)

    print(ans)


if __name__ == "__main__":
    main()