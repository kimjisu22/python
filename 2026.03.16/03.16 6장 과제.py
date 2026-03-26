##1. for문 이용하여 1부터 100가지 정수중 짝수의 합과 홀수의 합을 출력하는 프로그램을 작성하시오
##even = 0
##odd = 0
##
##for i in range(1, 101, 1):
##    if i % 2 == 0:
##        even += i
##    else:
##        odd += i
##
##print("1부터 100까지의 짝수의 합", even)
##print("1부터 100까지의 홀수의 합", odd)

## 2.while문 이용하여 1부터 100까지 정수 중 짝수의 합과 홀수의 합을 출력하는 프로그램을 작성하시오
##even = 0
##odd = 0
##i = 1
##
##while i <= 100:
##    if i % 2 == 0:
##        even += i
##    else:
##        odd += i
##    i += 1
##
##print("1부터 100까지의 짝수의 합: ", even)
##print("1부터 100까지의 홀수의 합: ", odd)

## 3. while문을 사용하여 1부터 100가지 정수중 3의 배수의 합을 구하는 프로그램을 작성하시오.

##sum = 0
##i = 1
##
##while i <= 100:
##    if i % 3 == 0:
##       sum += i
##    i+=1
##print("1부터 100까지 숫자 중 3의 배수의 합은?",sum)

## 4. 중첩 반복문을 사용하여 2 ~ 9단까지 구구단을 출력하는 프로그램을 작성하시오(출력시 f-string사용함, f-string의 역할: f를 문자열 앞에 붙이면 변수를 문자열 앞에 직접 삽입가능)
##print("************ 구구단 ************")
##for num in range(1, 10, 1):
##    for i in range(2, 10, 1):
##       print(f"{i}*{num}", end = "\t")
##    print('')

##5. 사칙 연산을 계산하는 프로그램을 작성하시오.
## 잘못된 메뉴가 선택되면, 선택하도록 메뉴를 보여주고 나눗셈의 경우 분모가 0인 경우 나눌 수 없다는 메세지를 출력하고 분모가 0이 아닌 경우에 나눗셈을 하도록 한다.
menu = 0
num1 = 0
num2 = 0
minus = 0
multi = 0
div = 0

menu = int(input("== 메뉴 ==\n1.덧셈\n2.뺄셈\n3.곱셈\n4.나눗셈\n==========="))
print('선택: ', menu)
if menu == 1:
    num1 = int(input("첫 번째 수 입력: "))
    num2 = int(input("첫 번째 수 입력: "))
    sum = num1 + num2
    print(f"{num1}+{num2}={sum}")        
if menu == 2:
    num1 = int(input("첫 번째 수 입력: "))
    num2 = int(input("첫 번째 수 입력: "))
    minus = num1 - num2
    print(f"{num1}-{num2}={minus}")        
if menu == 3:
    num1 = int(input("첫 번째 수 입력: "))
    num2 = int(input("첫 번째 수 입력: "))
    multi = num1 * num2
    print(f"{num1}*{num2}={multi}")        
if menu == 4:
    num1 = int(input("첫 번째 수 입력: "))
    num2 = int(input("첫 번째 수 입력: "))
    if num2 == 0:
        print("분모가 0이므로 나눌수 없습니다")
    else:
        div = num1 / num2
    print(f"{num1}/{num2}={div}")
else:
    menu = int(input("== 메뉴 ==\n1.덧셈\n2.뺄셈\n3.곱셈\n4.나눗셈\n==========="))
