# 1. 네 과목의 점수를 입력받습니다.
# input()으로 받은 값은 문자열이므로 int()를 써서 숫자로 바꿔줍니다.
kor = int(input("국어 점수를 입력하세요: "))
eng = int(input("영어 점수를 입력하세요: "))
math = int(input("수학 점수를 입력하세요: "))
sci = int(input("과학 점수를 입력하세요: "))

# 2. 평균을 계산합니다.
average = (kor + eng + math + sci) / 4

# 3. 합격 조건을 확인합니다.
# 모든 과목이 40점 이상이고(and), 평균이 60점 이상이어야 합니다.
if kor >= 40 and eng >= 40 and math >= 40 and sci >= 40:
    if average >= 60:
        print(f"평균 점수: {average}")
        print("결과: 합격입니다!")
    else:
        print(f"평균 점수: {average}")
        print("결과: 불합격입니다. (평균 60점 미만)")
else:
    print(f"평균 점수: {average}")
    print("결과: 불합격입니다. (40점 미만 과목 존재)")
    print(f"평균 점수: {average:.2f}")


