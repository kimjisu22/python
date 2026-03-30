def avgScore(*scores):
    print(type(scores))

    totalScore = 0
    cnt = len(scores)

    for score in scores:
        totalScore += score

    print('총점: ', totalScore, '점')
    print('평점: ', totalScore / cnt, '점')

print(avgScore(80, 90, 70))
print(avgScore(90, 85, 90, 100))
print(avgScore(95, 80, 95, 85))
