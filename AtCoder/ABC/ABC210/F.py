from scipy.spatial.distance import chebyshev
import numpy as np

a = np.array([1,1,1])
b = np.array([1,2,4])
print(chebyshev(a, b))