##7장 리스트 과제
## 2. 사용자로부터 리스트의 크기와 각 원소를 입력받은 후 찾고자 하는 특정값을 입력받아 순차검색을 수행하는 프로그램을 작성
## 리스트에 해당값이 존재하면 해당 인덱스를 출력하고, 값이 없으면 "찾을 수 없습니다"라는 메시지를 출력하기

a = []

list = int(input("리스트 크기 입력: "))

for n in range(1,list+1):
    a.append(int(input(f"{list}개의 정수를 입력하세요: ")))

find = int(input("찾을 값을 입력하세요: "))
for i in range(len(a)):
    idx = a.index(find)
    if a.index(find):
        print(f"{find}를 찾앗습니다. 인텍스는 {idx}입니다.")
    else:
        print("찾을 수 없습니다")
        

