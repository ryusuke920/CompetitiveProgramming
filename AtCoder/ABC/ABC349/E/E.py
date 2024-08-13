A = [list(map(int, input().split())) for _ in range(3)]
b = []
for i in range(3):
    for j in range(3):
        b.append(A[i][j])

b.sort(reverse=True)
ta, ao = 0, 0
for i in range(9):
    if i % 2 == 0:
        ta += b[i]
    else:
        ao += b[i]

if ta > ao:
    print("Takahashi")
else:
    print("Aoki")