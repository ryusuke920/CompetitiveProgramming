s = input()
ans = 0
left = '12345'
right = '67890'

for i, j in enumerate(s):
    if i == 0:
        ans += 500
    elif j == before:
        ans += 301
    else:
        if (j in left and before in left) or (j in right and before in right):
            ans += 210
        else:
            ans += 100
    before = j

print(ans)