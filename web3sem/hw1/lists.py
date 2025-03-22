arr = []

n = int(input())

for _ in range(n):
    command = input().split()
    operation = command[0]

    if operation == "insert":
        index = int(command[1])
        value = int(command[2])
        arr.insert(index, value)
    elif operation == "print":
        print(arr)

    elif operation == "remove":
        value = int(command[1])
        if value in arr:  # Проверяем, что элемент есть в списке
            arr.remove(value)
        else:
            print(f"Ошибка: элемент {value} отсутствует в списке")

    elif operation == "append":
        value = int(command[1])
        arr.append(value)
    elif operation == "sort":
        arr.sort()

    elif operation == "pop":
        if arr:  # Проверяем, что список не пустой
            arr.pop()
        else:
            print("Ошибка: нельзя выполнить pop на пустом списке")
    elif operation == "reverse":
        arr.reverse()