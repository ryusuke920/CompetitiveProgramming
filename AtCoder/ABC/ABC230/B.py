s = input()

t = ['oxx', 'xox', 'xxo']
if len(s) > 2:
    for i in range(len(s) - 2):
        if s[i : i + 3] not in t:
            exit(print('No'))
    print('Yes')
elif len(s) == 2:
    if s != 'oo':
        print('Yes')
    else:
        print('No')
else:
    print('Yes')