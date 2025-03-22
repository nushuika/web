def count_passengers(n, intervals, t):
    if n <= 0:
        print("Количество пассажиров должно быть положительным числом.")

    count = 0
    for entry, exit in intervals:
        if entry <= t <= exit:
            count += 1
    return count

n = int(input())

intervals = []
for _ in range(n):
    entry, exit = map(int, input().split())
    intervals.append((entry, exit))

t = int(input())

print(count_passengers(n, intervals, t))