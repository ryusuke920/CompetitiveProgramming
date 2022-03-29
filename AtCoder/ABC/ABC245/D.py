n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

import numpy

A = numpy.poly1d(a[::-1])
C = numpy.poly1d(c[::-1])

ans = []
for i in list(C/A)[0]:
  ans.append(int(i))
print(*ans[::-1])