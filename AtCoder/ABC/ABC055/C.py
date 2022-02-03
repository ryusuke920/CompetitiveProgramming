n,m = map(int,input().split())
count = 0
if m >= 2*n: #ex)3,6 4,15
    m -= 2*n
    count = n+(m//4)
#elif n <= m:  #ex)3,3 3,4 ,5 8
#    count = m//2
else:
    count = m//2
print(count)