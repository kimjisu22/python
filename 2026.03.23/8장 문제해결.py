##9-1 튜플의 아이템 조회
## 인덱스가 홀수인 아이템 조회하기

##sports = ('태권도', '야구','농구','축구','배구','권투','양궁')
##
##for index, item in enumerate(sports):
##    if index % 2 == 1:
##        print(index, ':', item)

##9-2 index()함수
names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')

for index, item in enumerate(name):
    if item == names:
        found = True
        break
if found == True:
    print(
inputData = input("검색하려는 이름을 입력하세요.: ")
print('이름: ', inputData, ', 인덱스: ', names.index(inputData))


