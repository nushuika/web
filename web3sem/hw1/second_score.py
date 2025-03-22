n = int(input())

if n > 1:
    scores = list(map(int, input().split()))

    max_score = max(scores)
    scores = [score for score in scores if score != max_score]

    second_max_score = max(scores)

    print(second_max_score)
else:
    print('Количество участников должно быть больше одного!')