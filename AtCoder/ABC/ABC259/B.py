import numpy as np

x, y, d = map(int, input().split())

cos = np.cos(np.deg2rad(d))
sin = np.sin(np.deg2rad(d))

ans_x = (x * cos) - (y * sin)
ans_y = (x * sin) + (y * cos)

print(ans_x, ans_y)