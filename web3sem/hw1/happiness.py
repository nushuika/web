def calculate_mood():

    n, m = map(int, input().split())
    if not (1 <= n <= 10 ** 5 and 1 <= m <= 10 ** 5):
        print("Ошибка: n и m должны быть в диапазоне от 1 до 10^5.")
        return

    array = list(map(int, input().split()))

    if not all(1 <= i <= 10 ** 9 for i in array):
        print("Ошибка: элементы массива должны быть в диапазоне от 1 до 10^9.")
        return

    A = set(map(int, input().split()))

    B = set(map(int, input().split()))

    mood = 0

    for i in array:
        if i in A:
            mood += 1
        elif i in B:
            mood -= 1

    print(mood)


calculate_mood()