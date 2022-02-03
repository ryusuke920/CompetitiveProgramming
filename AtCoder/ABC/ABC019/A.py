A, B, C = map(int,input().split()) 
if A>=B and A>=C and B>=C:
    print(B)
elif A>=B and A>=C and C>=B:
    print(C)
elif B>=A and B>=C and A>=C:
    print(A)
elif B>=A and B>=C and C>=A:
    print(C)
elif C>=A and C>=B and A>=B:
    print(A)
else :
    print(B)