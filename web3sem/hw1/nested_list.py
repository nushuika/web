n = int(input())

if n < 2 or n > 5:
    print("Количество учащихся должно быть от 2 до 5.")
else:
    students = []

    for _ in range(n):
        name = input()  
        score = float(input())  
        students.append([name, score])

    scores = sorted(set([student[1] for student in students]))

    if len(scores) < 2:
        print('Во вводимых данных всегда должен присутствовать хотя бы один учащийся со второй по величине оценкой.')
    else:
        second_highest_score = scores[1]

        second_highest_students = [student[0] for student in students if student[1] == second_highest_score]

        second_highest_students.sort()

        for name in second_highest_students:
            print(name)
