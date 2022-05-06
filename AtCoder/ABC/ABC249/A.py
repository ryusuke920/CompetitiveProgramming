a, b, c, d, e, f, x = map(int, input().split())

ta, ao = 0, 0
bt, ba = 0, 0
for i in range(1, x + 1):
    bt += 1
    ba += 1
    if bt <= d:
        ta += e
    if ba <= a:
        ao += b
    if bt == d + f:
        bt = 0
    if ba == a + c:
        ba = 0

if ta == ao:
    print('Draw')
elif ta > ao:
    print('Aoki')
else:
    print('Takahashi')