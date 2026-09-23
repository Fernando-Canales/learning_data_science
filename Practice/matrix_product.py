"""
Script that mutliplies matrices
Sept. 1 2026
Fernando Gutierrez Canales
"""

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 1], [1, 1]])
B = np.array([[1, 2], [3, 4]])

C = np.matmul(A,B)

print("A:", A)
print("B:", B)
print("A x B:", C)

#plt.imshow(A, cmap='viridis')
