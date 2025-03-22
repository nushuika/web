# Чтение строки из стандартного ввода
input_string = input()

# Разделение строки по пробелам и объединение с дефисами
result = '-'.join(input_string.split())

# Вывод результата
print(result)