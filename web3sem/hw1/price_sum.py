import csv

def calculate_total_expenses(filename: str):
    categories = {"Взрослый": 0, "Пенсионер": 0, "Ребенок": 0}

    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            categories["Взрослый"] += float(row["Взрослый"])
            categories["Пенсионер"] += float(row["Пенсионер"])
            categories["Ребенок"] += float(row["Ребенок"])

    return categories

filename = "products.csv"
total_expenses = calculate_total_expenses(filename)

print(f"{total_expenses['Взрослый']:.2f} {total_expenses['Пенсионер']:.2f} {total_expenses['Ребенок']:.2f}")