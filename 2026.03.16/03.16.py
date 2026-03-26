##1부터 10까지 홀수
##for num in range(1, 10, 2):
##    print('1부터 10까지 홀수: ', num)

##7-2 사용자가 입력한 횟수만큼 '메일발송!' 문자열 출력하기
##num = int(input('메일 발송 횟수를 입력하세요. '))
##
##for num in range(1, num+1, 1):
##    print('메일 발송!')

##7-3 3의 배수 출력하기
##for num in range(3, 11, 2):
##    print('3의 배수: ' , num)

##7-4 구구단 5단 출력하기
##for num in range(1, 10, 1):
##    print(5, end = '')
##    print('*', end = '')
##    print(num, end = '')
##    print('=', end = '')
##    print(5 * num)

##1부터 10까지 합
##1부터 10까지  홀수의 합
##1부터 10까지 짝수의 합
##수업시간 풀이
##sum = 0
##even = 0
##odd = 0
##
##for i in range(1, 11, 1):
##    sum += i
##    if i % 2 == 0:
##        even += i
##    else:
##        odd+=i
##
##print("1부터 10까지의 합",sum)
##print("1부터 10까지의 홀수의 합", even)
##print("1부터 10까지의 짝수의 합", odd)

##for i in range(10, 0, -1):
##    print(i)

## 1부터 10까지 출력 for문으로
##for i in range(1, 11, 1):
##    print(i)
    
## 1~10까지 출력하기

## 1~10까지 합, 홀수의 합, 짝수의 합 while문으로
##sum = 0
##even = 0
##odd = 0
##i = 1
##
##while i <= 10:
##    sum += i
##    if i % 2 == 0:
##        even += i
##    else:
##        odd += i
##    i+=1
##                         
##print("1부터 10까지의 합: ",sum)
##print("1부터 10까지의 짝수의 합: ", even)
##print("1부터 10까지의 홀수의 합: ", odd)

## 중첩 반복문을 이용하여 별찍기
##for num1 in range(1, 6):
##    for num2 in range(num1):
##            print('*', end='')
##    print()

##시스템 관리자 로그인 기능을 만들어봅시다

id = 0
pw = 0
cnt = 1
while True:
    if cnt > 5:
        print('로그인 실패')
        break
    

## 교수님 풀이
##adminPw = 'hanbitac'
##count = 1
##
##while True:
##    if count > 5:
##            print('로그인 실패!! 횟수 초과!!!')
##            break
##        inputPw = input('관리자가 암호를 입력하세요. ')
##
##        if inputPw != adimPw:
##            print('암호를 다시 확인하세요!')
##            count += 1
##        elif inputPw == adminPw:
##            print('로그인 됐습니다.')
##            break

