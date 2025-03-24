import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Perform basic operations
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

# Reshape an array
matrix = np.arange(1, 10).reshape(3, 3)
print("\n3x3 Matrix:\n", matrix)

# Matrix multiplication
matrix2 = np.array([[2, 0, 1], [3, 5, 2], [4, 1, 3]])
result = np.dot(matrix, matrix2)
print("\nMatrix Multiplication:\n", result)
