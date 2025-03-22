def minion_game(s):
    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    n = len(s)
    for i in range(n):
        if s[i] in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i

    if kevin_score > stuart_score:
        print(f"Кевин {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Стюарт {stuart_score}")

s = input()

if len(s) == 0 or len(s) > 10**6:
    print("Ошибка: длина строки должна быть от 1 до 10^6 символов.")
else:
    minion_game(s)