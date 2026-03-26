## 7장 리스트 과제
## 1. 다음은 홍길동 수험생의 시험성적을 키보드로부터 입력받고 아래 합격기준을 참조하여 합격여부를 판단하는 프로그램을 작성하시오
## 합격기준
##각 과목은 100점을 만점으로하여 각 과목은 40점이상이어야 한다.
##전과목의 평균은 60점 이상이어야 한다.

score = []
x = []
total = 0
avg = 0

for n in range(1,7):
    score.append(int(input(f"{n}번째 시험성적을 입력하시오: ")))

for i in range(len(score)):
    if score[i] < 40:
        x.append(score[i])
    total += score[i]
    
avg = total/len(score)
print("40점 미만의 과목수: ",len(x))
print("평균점수: ", avg)

if len(x) > 0:
    print("불합격")
else:
    print("합격")


        


