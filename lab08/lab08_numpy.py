import numpy as np

#1
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)
print()

#2
print(hours[2])
print(hours[-1])
print(hours[2:6])
print(hours[::2])
print(hours[::-1])
print()
#3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18]
])

print(temperatures.shape)
print(temperatures.ndim)
print(temperatures.size)
print(temperatures[1, :])
print(temperatures[:, 2])
print(temperatures[0, :])
print(temperatures[:, -1])
print(temperatures[:2, 1:])
print(temperatures[0:2, 1:3])
print()
#4
matrix = np.arange(1, 26).reshape(5, 5)

a = matrix[:3, :]
print(a, a.shape)

b = matrix[-2:, :]
print(b, b.shape)

c = matrix[:, :2]
print(c, c.shape)

d = matrix[1:4, 2:5]
print(d, d.shape)
print()

#5
changed_hours = hours.copy()

changed_hours[2:5] = 99
changed_hours[::2] = -1

print("Изменённый массив:", changed_hours)
print("Исходный массив:", hours)
print()

matrix = np.arange(25).reshape(5, 5)

changed_matrix = matrix.copy()

changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("Изменённая матрица:")
print(changed_matrix)

print("Исходная матрица:")
print(matrix)
print()
#6
numbers = np.arange(0, 12)

table = numbers.reshape(3, 4)

transposed = table.T

print("numbers:")
print(numbers)

print("table:")
print(table)

print("transposed:")
print(transposed)

print("Форма numbers:", numbers.shape)
print("Форма table:", table.shape)
print("Форма transposed:", transposed.shape)