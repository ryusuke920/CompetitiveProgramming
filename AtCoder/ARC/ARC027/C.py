import sys
input = sys.stdin.readline

x, y = map(int, input().split())
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j][k] := i 番目の商品を買うか買わないとき、スペシャルチケットの残りが x枚, チケットが y 枚のときの嬉しさの最大値
dp = [[[0] * (601) for _ in range(2)] for _ in range(n + 1)]
