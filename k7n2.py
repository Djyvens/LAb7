import random

def generate_lists(matrix):
    n = len(matrix)
    x = []
    y = []
    for i in range(n):
        for j in range(n):
            if j>= i:
                x.append(matrix[i][j])
            else:
                y.append(matrix[i][j])
    return x, y

matrix_size = random.randint(2, 10)
matrix = [[random.randint(2, 10) for j in range(matrix_size)] for i in range(matrix_size)]

for x in matrix:
    print(x)

result_X, result_Y = generate_lists(matrix)
print("X (Верхний треугольник):", result_X)
print("Y (Нижний треугольник):", result_Y)

