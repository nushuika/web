def multiply_matrices():
    n = int(input())

    if not (2 <= n <= 10):
        print("Ошибка: размерность матрицы должна быть в диапазоне от 2 до 10.")
        return
    A = []
    for _ in range(n):
        row = list(map(int, input().split()))
        if len(row) != n:
            print(f"Ошибка: строка матрицы должна содержать ровно {n} чисел.")
            return
        A.append(row)

    print()
    B = []
    for _ in range(n):
        row = list(map(int, input().split()))
        if len(row) != n:
            print(f"Ошибка: строка матрицы должна содержать ровно {n} чисел.")
            return
        B.append(row)

    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    print()
    for row in C:
        print(" ".join(map(str, row)))

multiply_matrices()