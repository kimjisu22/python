##6-2 p.18
##num = int(input('숫자를 입력하세요.'))
##
##if num > 10:
##          print('num은 10보다 크다.')
##          print('num :',num)
##
##num = int(input('정수를 입력하세요.'))

## 6-6 p.26
##score = int(input('점수를 입력하세요.'))
##
##if score >= 80:
##    print('합격입니다.')
##else:
##    print('아쉽습니다. 다시 도전해주세요.')

##홀짝 
##num = int(input('숫자를 입력하세요.'))
##if num % 2 == 0:
##    print('짝수입니다.')
##else:
##    print('홀수입니다.')

##if elif문 6-9 p.34
##score = int(input('점수를 입력하세요.'))
##
##if score >= 90:
##    print('A')
##
##elif score >= 80:
##    print('B')
##
##elif score >= 70:
##    print('C')
##
##elif score >= 60:
##    print('D')
##
##else:
##    print('F')


##다음 요구사항을 충족하는 프로그램을 if-elif문을 이용하여 만드시오
##BMI지수를 입력한다.
##BMI지수가 140초과이면 고도비만
##BMI지수가 120초과 ~ 140이하이면 비만
##BMI지수가 110초과 ~ 120이하이면 과체중
##BMI지수가 110초과 ~ 120이하이면 정상체중
##BMI지수가 90초과 ~ 110이하이면 저체중
    

##BMI = int(input('BMI지수를 입력하시오.'))
##if BMI > 140:
##        print('고도비만')
##elif BMI>120 and BMI<=140:
##        print('비만')
##elif BMI>110 and BMI<=120:
##        print('과체중')
##elif BMI>90 and BMI<=110:
##        print('정상체중')
##else:
##        print('저체중')

##6-5 p.44        
##print('1.월~금, 2.토요일, 3.공휴일')
##dayweek = int(input('요일을 선택하세요.'))
##
##if dayweek == 1:
##    print('버스 전용차로 단속 중입니다.')
##    print('1.버스, 2.승용차')
##    carType = int(input('차종을 선택하세요.'))
##
##    if carType != 1:
##            print('버스 전용차로 위반!!')
##    else:
##            print('버스입니다.')
##else:
##    print('토요일 및 공휴일은 단속하지 않습니다.')

#p.45
endBirthYear = int(input('출생 연도 끝자리 입력 : '))
age = int(input('만 나이 입력: '))
if age < 65:
    if endBirthYear % 5 == 1: 
        print('월요일에 구매 가능합니다.')

    elif endBirthYear % 5 == 2: 
        print('화요일에 구매 가능합니다.')
        
    elif endBirthYear % 5 == 3:
        print('수요일에 구매 가능합니다.')

    elif endBirthYear % 5 == 4:
        print('목요일에 구매 가능합니다.')

    else:
        print('금요일에 구매 가능합니다.')
else:
    print('언제든지 구매 가능합니다.')
