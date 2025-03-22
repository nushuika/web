def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year = int(input())
if 1900 <= year <= 10**5:
    print(is_leap_year(year))
else:
    print("Ошибка: год должен быть в диапазоне от 1900 до 10^5.")
