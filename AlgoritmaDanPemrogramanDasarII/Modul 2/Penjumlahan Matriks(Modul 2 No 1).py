import numpy as np

# Input elemen matriks A
print("Masukkan elemen matriks A (2x3):")
A = np.array([[int(input(f"A[{i}][{j}]: ")) for j in range(3)] for i in range(2)])

# Input elemen matriks B
print("Masukkan elemen matriks B (2x3):")
B = np.array([[int(input(f"B[{i}][{j}]: ")) for j in range(3)] for i in range(2)])

# Menjumlahkan matriks A dan B
C = A + B

# Menampilkan hasil
print("\nMatriks A:")
print(A)
print("\nMatriks B:")
print(B)
print("\nHasil penjumlahan matriks A dan B:")
print(C)
