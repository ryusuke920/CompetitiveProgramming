import sys
input = sys.stdin.readline

M, S, T, L = map(int,input().split())
t = [list(map(int,input().split())) for _ in range(M)]
x = list(map(int,input().split()))
n = list(map(int,input().split()))

"""
出力
K
p1 p2 ... pK

"""