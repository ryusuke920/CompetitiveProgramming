s = input()
for i in range(len(s) - 2):
    if s[i : i + 3] == 'OOO':
        exit(print('East'))
    if s[i : i + 3] == 'XXX':
        exit(print('West'))

print('NA')