n = int(input())

if 1 <= n <= 20:
    for i in range(n):
        print(i ** 2)
else:
    print("Число должно быть в диапазоне от 1 до 20!")
