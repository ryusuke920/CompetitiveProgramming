from typing import Sized


n = int(input())
print(0)
l, r = 0, n
sl = sr = input()
if sl == "Vacant":
    exit()

while True:
    mid = (l + r) // 2
    print(mid)
    s = input()
    if mid == "Vacant":
        exit()
    if (s != sl) != ((mid - l) % 2 == 0):
        l, sl = mid, s
    else:
        r, sr = mid, s