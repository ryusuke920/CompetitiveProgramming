n = int(input())
st = []

for i in range(n):
    s, t = input().split()
    st.append([s, t])

for i in range(n):
    if st.count(st[i]) >= 2:
        exit(print('Yes'))

print('No')