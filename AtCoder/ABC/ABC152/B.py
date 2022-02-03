a,b = map(int,input().split())
ans_a = str(b)*a
ans_b = str(a)*b
print(min(ans_a,ans_b))