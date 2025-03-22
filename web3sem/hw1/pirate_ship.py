def pirate_loot():
    n, m = map(int, input().split())

    items = []
    for _ in range(m):
        name, weight, value = input().split()
        weight = int(weight)
        value = int(value)
        value_per_weight = value / weight
        items.append((name, weight, value, value_per_weight))

    items.sort(key=lambda x: x[3], reverse=True)

    cargo = []
    remaining_capacity = n
    for name, weight, value, value_per_weight in items:
        if remaining_capacity == 0:
            break
        if weight <= remaining_capacity:
            cargo.append((name, weight, value))
            remaining_capacity -= weight
        else:
            fraction = remaining_capacity / weight
            cargo_weight = remaining_capacity
            cargo_value = round(value * fraction, 2)
            cargo.append((name, cargo_weight, cargo_value))
            remaining_capacity = 0

    for name, weight, value in cargo:
        print(f"{name} {weight:.2f} {value:.2f}")

pirate_loot()