from collections import defaultdict

n = int(input())
card = list(input().split())

d = defaultdict(int)
d_rev = defaultdict(str)

d['A'] = 1
d['T'] = 10
d['J'] = 11
d['Q'] = 12
d['K'] = 13
d_rev[1] = 'A'
d_rev[10] = 'T'
d_rev[11] = 'J'
d_rev[12] = 'Q'
d_rev[13] = 'K'

judge = [[False] * 13 for _ in range(4)]
for i in card:
    type_, num = str(i)[0], str(i)[1]
    if type_ == 'D':
        if num in  'ATJQK':
            num = d[num]
        else:
            num = int(num)
        judge[0][num - 1] = True

    if type_ == 'C':
        if num in  'ATJQK':
            num = d[num]
        else:
            num = int(num)
        judge[1][num - 1] = True

    if type_ == 'H':
        if num in  'ATJQK':
            num = d[num]
        else:
            num = int(num)
        judge[2][num - 1] = True

    if type_ == 'S':
        if num in  'ATJQK':
            num = d[num]
        else:
            num = int(num)
        judge[3][num - 1] = True

ans = []
for i in range(4):
    for j in range(13):
        if judge[i][j]:
            key_ = ''
            if i == 0: key_ += 'D'
            if i == 1: key_ += 'C'
            if i == 2: key_ += 'H'
            if i == 3: key_ += 'S'
            
            if j == 0 or j >= 9:
                key_ += d_rev[j + 1]
            else:
                key_ += str(j + 1)
            ans.append(key_)

print(*ans)