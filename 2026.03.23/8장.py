fruits=('사과','포도','수박','참외')
print(type(fruits))
print(fruits[3])
print(fruits.index('수박'))

##9-1
sports = ('태권도', '야구', '농구')
print(sports.index('야구'))

##9-2
##name = ('박찬호', '이승엽', '박세리', '박지성', '이순철','선동열','손흥민','김연아')
##inputData = input("검색하려는 이름을 입력하세요.: ")
##found=False

## in, not in
##for index, item in enumerate(name):
##    if item== inputData:
##        found = True
##        break
##if found == True:
##    print(f"{inputData}는 목록에 있으며, 인덱스는 {index}입니다")
##else:
##    print("찾고자 하는 이름이 없습니다.")

##9-3
##colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Puple')
##print('Green' in colors)
##
##print('Green' not in colors)

## 튜플 리스트 변환 (수정하려고)
##colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Puple')

##정렬
##colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Puple')
##print(colors)
##
##cs = sorted(colors)
##print(cs)
##print('cs의 자료형: ',type(cs))
##ages = {'박찬호':48,'박지성':40,'박세리':50}
##print(ages['박지성'])

## 수정
dicContainer = {'이름':'홍길동', '나이':25, '주소':'서대문구 연희로', '취미':['축구','수영','조깅'],'몸무게':85.3}
##dicContainer['이름']= '둘리'
##dicContainer['나이']= '10'
##dicContainer['주소']= '쌍문동'

##print(dicContainer)

##삭제
##del dicContainer['몸무게']
##print(len(dicContainer))

## 딕셔너리에서 전체 키와 값을 조회

for key in dicContainer.keys():
    print(key, '\t:', dicContainer[key])




