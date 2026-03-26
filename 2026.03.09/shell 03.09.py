Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
userData = int('정수를 입력하세요.')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    userData = int('정수를 입력하세요.')
ValueError: invalid literal for int() with base 10: '정수를 입력하세요.'
userData = input('정수를 입력하세요.')
정수를 입력하세요.10

type(userData)
<class 'str'>
userData = input('정수를 입력하세요')
정수를 입력하세요20
userData = int(userData)
type(userData)
<class 'int'>
print('아이디 및 비밀번호 확인')
아이디 및 비밀번호 확인
print('홍길동 고객님 안녕하세요.')
홍길동 고객님 안녕하세요.
print('고객님의 아이디와 비밀번호는 아래와 같습니다.')
고객님의 아이디와 비밀번호는 아래와 같습니다.
id = intput('아이디를 입력하세요')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    id = intput('아이디를 입력하세요')
NameError: name 'intput' is not defined. Did you mean: 'input'?
id = input('아이디를 입력하세요')
아이디를 입력하세요
gildong
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    gildong
NameError: name 'gildong' is not defined
id = str(id)
id = gildong
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    id = gildong
NameError: name 'gildong' is not defined
id = input('gildong')
gildong
pw = input('1234
           
SyntaxError: unterminated string literal (detected at line 1)
pw = input('1234')
           
1234
print(id,pw)
           
 
print(id)
           

print(userName, '고객님 안녕하세요')
           
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(userName, '고객님 안녕하세요')
NameError: name 'userName' is not defined. Did you mean: 'userData'?
userName = '홍길동'
           
id = input('이름을 입력하세요.')
           
이름을 입력하세요.홍길동
print(id)
           
홍길동
print(id, '고객님 안녕하세요.')
           
홍길동 고객님 안녕하세요.
userName = input('이름을 입력하세요.')
           
이름을 입력하세요.홍길동
print(id, '고객님 안녕하세요.')
           
홍길동 고객님 안녕하세요.
print(userName, '고객님 안녕하세요.')
           
홍길동 고객님 안녕하세요.
id = input('아이디를 입력하세요.')
           
아이디를 입력하세요.gildong
print(id, ':gildong')
           
gildong :gildong
print(id, '아이디:')
           
gildong 아이디:
print('아이디:',id)
           
아이디: gildong
pw = input('비밀번호를 입력하세요.')
           
비밀번호를 입력하세요.1234
print('비밀번호': pw)
           
SyntaxError: invalid syntax
print('비밀번호':,pw)
           
SyntaxError: invalid syntax
print('비밀번호:',pw)
           
비밀번호: 1234
print('아이디 및 비밀번호 확인')
           
아이디 및 비밀번호 확인
print('홍길동 고객님의 아이디와 비밀번호는 아래와 같습니다.')
           
홍길동 고객님의 아이디와 비밀번호는 아래와 같습니다.
print('아이디':,id)
           
SyntaxError: invalid syntax
print('아이디:',id)
           
아이디: gildong
print('비밀번호:',pw)
           
비밀번호: 1234
userName = '고길동'
           
userName = input('이름을 입력하세요')
           
이름을 입력하세요고길동
id = input('아이디를 입력하세요: ')
           
아이디를 입력하세요: gildong
pw = input('비밀번호를 입력하세요: ')
           
비밀번호를 입력하세요:  gildong
id = input('비밀번호를 입력하세요: ')
           
비밀번호를 입력하세요: 1234
print('아이디 및 비밀번호 확인')
           
아이디 및 비밀번호 확인
print(userName, '고객님 안녕하세요.')
           
고길동 고객님 안녕하세요.
print(userName, '고객님의 아이디와 비밀번호는 아래와 같습니다.')
           
고길동 고객님의 아이디와 비밀번호는 아래와 같습니다.
print(id, '아이디: ')
           
1234 아이디: 
id = input('아이디를 입력하세요: ')
           
아이디를 입력하세요: gildong
print(id, '아이디: ')
           
gildong 아이디: 
print('아이디: ',id)
           
아이디:  gildong
pw = input('비밀번호를 입력하세요: ')
           
비밀번호를 입력하세요: 1234
print(pw, '비밀번호: ')
           
1234 비밀번호: 
print('비밀번호: ', pw)
           
비밀번호:  1234

==== RESTART: C:/Users/AI-00/AppData/Local/Programs/Python/Python313/test.py ===
이름을 입력하세요.홍길동
홍길동 고객님 안녕하세요.

==== RESTART: C:/Users/AI-00/AppData/Local/Programs/Python/Python313/test.py ===
이름을 입력하세요.
==== RESTART: C:/Users/AI-00/AppData/Local/Programs/Python/Python313/test.py ===
이름을 입력하세요.홍길동
홍길동 고객님 안녕하세요.
아이디를 입력하세요: gildong
gildong 아이디:

==== RESTART: C:/Users/AI-00/AppData/Local/Programs/Python/Python313/test.py ===
이름을 입력하세요.홍길동
홍길동 고객님 안녕하세요.
아이디를 입력하세요: gildong
아이디: gildong

==== RESTART: C:/Users/AI-00/AppData/Local/Programs/Python/Python313/test.py ===
이름을 입력하세요.홍길동
홍길동 고객님 안녕하세요.
아이디를 입력하세요: gildong
아이디: gildong
비밀번호를 입력하세요: 1234
비밀번호:  1234

========================== RESTART: D:/03.09  ch05.py ==========================
1월 매출: 300000000
2월 매출: 280000000
3월 매출: 290000000
1분기 전체 매출:  870000000 원

========================== RESTART: D:/03.09  ch05.py ==========================
1월 매출: 
Traceback (most recent call last):
  File "D:/03.09  ch05.py", line 1, in <module>
    sales1 = int(input('1월 매출: '))
ValueError: invalid literal for int() with base 10: ''



====================== RESTART: D:/python 자료구조/조건식p.76.py ======================
점수를 입력하세요.70
시험결과: 합격

====================== RESTART: D:/python 자료구조/조건식p.76.py ======================
점수를 입력하세요.73
점수를 입력하세요.40
점수를 입력하세요.20
점수를 입력하세요.20
점수를 입력하세요.20
Traceback (most recent call last):
  File "D:/python 자료구조/조건식p.76.py", line 8, in <module>
    result = '합격' if myScore >= 60 else '불합격'
NameError: name 'myScore' is not defined. Did you mean: 'myScore1'?

====================== RESTART: D:/python 자료구조/조건식p.76.py ======================
점수를 입력하세요.20
점수를 입력하세요.20
점수를 입력하세요.20
점수를 입력하세요.20
점수를 입력하세요.20
시험결과: 불합격

====================== RESTART: D:/python 자료구조/조건식p.76.py ======================
점수를 입력하세요.90
점수를 입력하세요.90
점수를 입력하세요.90
점수를 입력하세요.90
점수를 입력하세요.90
시험결과: 합격

====================== RESTART: D:/python 자료구조/과제03.09.py ======================
금액을 입력하세요: 50000
만원:  5

====================== RESTART: D:/python 자료구조/과제03.09.py ======================
금액을 입력하세요: 50000
만원: 매 5

====================== RESTART: D:/python 자료구조/과제03.09.py ======================
금액을 입력하세요: 50000
만원:  5 매

====================== RESTART: D:/python 자료구조/과제03.09.py ======================
금액을 입력하세요: 
====================== RESTART: D:/python 자료구조/과제03.09.py ======================
금액을 입력하세요: 50000
만원:  5 매
만원:  1 매

====================== RESTART: D:/python 자료구조/과제03.09.py ======================
금액을 입력하세요: 50000
오만원:  1 매
만원:  5 매

====================== RESTART: D:/python 자료구조/과제03.09.py ======================
금액을 입력하세요: 65750
오만원:  1 매
만원:  6 매

====================== RESTART: D:/python 자료구조/과제03.09.py ======================
금액을 입력하세요: 65750
Traceback (most recent call last):
  File "D:/python 자료구조/과제03.09.py", line 15, in <module>
    print('오만원: ', manwon5, '매')
NameError: name 'manwon5' is not defined

====================== RESTART: D:/python 자료구조/과제03.09.py ======================
금액을 입력하세요: 65750
오만원:  1 매
만원:  6 매
오천원:  13 매
천원:  65 매
백원:  657 매
오십원:  1315 매
십원:  6575 매
일원:  65750 매

====================== RESTART: D:/python 자료구조/과제03.09.py ======================
금액을 입력하세요: 
====================== RESTART: D:/python 자료구조/과제03.09.py ======================
금액을 입력하세요: 65750
오만원:  1 매
만원:  6 매
오천원:  13 매
천원:  65 매
백원:  657 개
오십원:  1315 개
십원:  6575 개
일원:  65750 개
>>> 
====================== RESTART: D:/python 자료구조/과제03.09.py ======================
금액을 입력하세요: 65750
오만원:  1 매
만원:  1 매
오천원:  1 매
천원:  0 매
백원:  7 개
오십원:  1 개
십원:  0 개
일원:  0 개
>>> 
====================== RESTART: D:/python 자료구조/과제03.09.py ======================
금액을 입력하세요: 65750
오만원:  1 매
  만원:  1 매
오천원:  1 매
  천원:  0 매
  백원:  7 개
오십원:  1 개
  십원:  0 개
  일원:  0 개
>>> 
====================== RESTART: D:/python 자료구조/과제03.09.py ======================
금액을 입력하세요: 65750
오만원:  1 매
  만원:  1 매
오천원:  1 매
  천원:  0 매
오백원:  1 개
  백원:  2 개
오십원:  1 개
  십원:  0 개
  일원:  0 개
