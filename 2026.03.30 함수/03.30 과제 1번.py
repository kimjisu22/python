# 1. 함수를 활용하여 사칙연산 기능을 구현하고, 사용자 입력을 받아 동작하는 계산기를 작성하고자 한다.
#  - 덧셈, 뺄셈, 곱셈, 나눗셈 함수를 각각 만들며, 사용자가 연산자와 숫자를 입력하면 결과를 출력한다.
#  - while 문을 사용하여 사용자가 'exit' 입력 시까지 반복 실행된다. 
#  - split()  함수 사용 (파일명 9-1.py)


#함수생성
def add (Num1,Num2):
    print(f'{Num1}+{Num2}={Num1+Num2}')
def sub (Num1,Num2):
    print(f'{Num1}+{Num2}={Num1+Num2}')
def mul (Num1,Num2):
    print(f'{Num1}+{Num2}={Num1+Num2}')
def div (Num1,Num2):
    print(f'{Num1}+{Num2}={Num1+Num2}')
inpuData = 0

   # 입출력
while True:
    if inpuData.islower == 'exit':
        break

    inpuData = int(input("원하는 계산식을 입력하세요(예:5+3) 5+10: "))
    parts = inpuData.split()
    num1 , operator ,num2 = parts
    Num1 =int(num1)
    Num2 =int(num2)
    


#함수호출부
if '+' == operator:
   add(Num1,Num2)
elif '-' == operator:
   sub(Num1,Num2)
elif '-' == operator:
   mul(Num1,Num2)
else:
   div(Num1,Num2)
