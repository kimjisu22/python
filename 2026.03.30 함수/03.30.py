# 예제2 계산기 프로그램
while True:
    num1 = int(input("첫번재 숫자를 입력하세요"))
    num2 = int(input("두번째 숫자를 입력하세요"))
    choose = int(input("연산자를 선택하세요. 1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈"))

    def tot():
        print("덧셈 결과: ", num1 + num2)

    def minus():
        print("뺄셈 결과: ", num1 - num2)

    def multiple():
        print("곱셈 결과: ", num1 * num2)

    def div():
        print("나눗셈 결과: ", num1 / num2)

    if choose == 1:
        tot()
    
    elif choose == 2:
        minus()    
    
    elif choose == 3:
        multiple()

    elif choose == 4:
        div()

    else:
        break



    

