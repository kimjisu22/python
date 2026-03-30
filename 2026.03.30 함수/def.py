# def greet():
#     print("안녕하세요")
#     print("Nice to meet you")
# greet()

# def convertUnit():
#     print(lengthCm, 'cm = ', lengthCm * 0.393701, 'inch')

#     lengthCm = float(input('길이를 입력하세요.(cm)'))
#     convertUnit()

# def calculateDistance():
#     print("이동 거리는", hourData * speedData, "km 입니다")

#     hourData = float(input("이동시간을 입력하세요."))
#     speedData = float(input("이동 속도를 입력하세요"))
#     calculateDistance()

# 예제2 계산기 프로그램
num1 = int(input("첫번재 숫자를 입력하세요"))
num2 = int(input("두번째 숫자를 입력하세요"))
choose = int(input("연산자를 선택하세요. 1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈"))

if choose == 1:
    sum()
    
elif choose == 2:
    minus()    
    
elif choose == 3:
    multiple()

elif choose == 4:
    div()

else:
    print("연산자를 다시 선택해주세요")


def sum():
    print("덧셈 결과: ", num1 + num2)

def minus():
    minus = num1 - num2
    print("뺄셈 결과: ", minus)
    
def multiple():
    multiple = num1 * num2
    print("곱셈 결과: ", multiple)

def div():
    div = num1 / num2
    print("나눗셈 결과: ", div)

 
  