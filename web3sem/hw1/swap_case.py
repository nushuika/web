s = input()

if 0 < len(s) <= 1000:
    result = s.swapcase()
    print(result)
else:
    print("Ошибка: длина строки должна быть больше 0 и не превышать 1000 символов.")
