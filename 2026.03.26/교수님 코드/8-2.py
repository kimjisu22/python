#8-2

scores=(
       ("철수",85),
       ("영희",90),
       ("민수",78),
       ("지혜",88)
       )

totalscore=0
flag=False

for score in scores:
    totalscore+=score[1]
print(f'전체 학생의 평균점수는 {totalscore/len(scores)}입니다.')

name=input('성적을 확인할 학생의 이름을 입력하세요')

for score in scores:
    if name==score[0]:
       flag=True
       break

if flag:
    print(f'{score[0]}의 점수는 {score[1]}점 입니다.')
else:
    print('해당학생이 없습니다.')

