##2. 학생들의 성적을 튜플로 저장하고, 평균 점수를 계산하는 프로그램을 작성하고자 한다. 학생 이름과 성적을 튜플로 저장하고, 모든 학생의 평균 점수를 계산한다. 또한 특정학생의 성적을 조회할 수 있도록 하시오.

result = (['철수',85],['영희',90],['민수',78],['지혜',88])

sum = 0

for student in result:
    sum += student[1]
avg = sum / len(result)
print("전체 학생의 평균 점수: ", avg)

found = False

name = input("성적을 확인할 학생의 이름을 입력하세요: ")

for index, item in enumerate(result):

    if item[0] == name:
        found = True
if found:
    print(f"{name}의 점수는 {item[1]}입니다")
else:
    print("해당 학생이 없습니다")

