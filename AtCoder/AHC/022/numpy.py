import numpy as np

def f(sigma):
    # 正規分布から値をサンプリング
    sampled_value = np.normal(0, sigma)
    return sampled_value

# 標準偏差が1の場合のサンプリング
sampled_result = f(1)
print("Sampled value:", sampled_result)