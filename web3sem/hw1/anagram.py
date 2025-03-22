def are_anagrams(str1, str2):
    if " " in str1 or " " in str2:
        return "В строках не должно быть пробелов!"

    if sorted(str1) == sorted(str2):
        return "YES"
    else:
        return "NO"

str1 = input()
str2 = input()

print(are_anagrams(str1, str2))