myScore1 = int(input('점수를 입력하세요.'))
myScore2 = int(input('점수를 입력하세요.'))
myScore3 = int(input('점수를 입력하세요.'))
myScore4 = int(input('점수를 입력하세요.'))
myScore5 = int(input('점수를 입력하세요.'))
sum = myScore1 + myScore2 + myScore3 + myScore4 + myScore5
avg = sum / 5
result = '합격' if avg >= 60 else '불합격'
print('시험결과: ' + result)
20
