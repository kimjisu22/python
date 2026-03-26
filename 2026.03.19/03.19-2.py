## 홀수출력
##fruits = ['사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나']
##
##for i in range(1,len(fruits),2):
##    print(fruits[i])

## 8-1
##message = input('메세지를 입력하세요.')
##print(len(message))

## 8-2
##balls = ['야구공', '축구공', '탁구공', '골프공', '농구공']
##
##for item in balls:
##    print('item: ', item)

## 8-3
##balls = ['야구공','축구공','탁구공','골프공','농구공']
##
##for index, item in enumerate(balls):
##    print('index: ', index, ',item: ', item)
##
##message = input('메세지를 입력하세요.')
##print(len(message))

##8-4
##balls = ['야구공','축구공','탁구공','골프공','농구공']
##i = 0
##
##while i <len(balls):
##    print(balls[i])
##    i += 1

##numbers = [10,20,30,40,50]
##print(numbers)
##print(numbers.index(20))

##
##index()함
##str = 'python'
##print(str.index('th'))

##append
##hobby = ['독서','등산','요리']
##print('홍길동 학생의 취미 : ',hobby)
##
##hobby.append('배구')
##print('홍길동 학생의 취미 : ',hobby)

##
##for index, item in enumerate(hobby):
##    print('index:', index,'item:' , item)
##
##hobby.insert(2,'음악감상')
##print(hobby)
##
##print(len(hobby))

## while문으로 바꾼거 오류 해결바람

##languages = ['c++','c#','java','python']
##
##str = 0
##num = 0
##while str <= len(languages):
##    if str == 'java':
##        languages.remove('java')
##        print(languages)
##        
##    else:
##        print(languages)

    
##for str in languages:
##    if str == 'java':    
##        languages.remove('java')
##print(languages)

##animals = ['호랑이','사자','곰','여우','늑대']
##print(animals[:4])

## 2차원 리스트 - 중첩 for문
##numList2 = [[1,2,3,4],
##            [5,6,7,8],
##            [9,10,11,12]]
##
##for i in range(0,3) :
##    for k in range(0,4) :
##        print(" ", numList2[i][k], end='')
##    print('')

