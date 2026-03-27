# 사용자의 연락처를 저장하고 검색할 수 있는 연락처 관리 프로그램 작성
# 이름: 전화번호 형태의 딕셔너리를 사용하고 새로운 연락처를 추가가 가능해야 하며 이름을 입력하면 전화번호를 조회할 수 있도록 한다.

tel = {'철수': '010-1111-1111', '영희': '010-2222-2222', '민수': '010-3333-3333', '지혜':'010-4444-4444' }

add = int(input("1.연락처 추가\n2.연락처 조회\n3.종료\n메뉴를 선택하세요: "))
i = 1

while i < len(tel):
    i+=1
    if add == 1:
        name = input("이름을 입력하세요: ")
        phone = input("전화번호를 입력하세요: ")
        tel[name] = phone
        
        print(f"{name}의 연락처가 저장되었습니다.")
        print(tel.keys(), tel.values())
    
        break
        
    elif add == 2:
        select = input("조회할 이름을 입력하세요: ")
        print(f"{select}의 전화번호: ",) 
        
        break

    elif add == 3:
        print("프로그램을 종료합니다")
        
else:
    print("올바른 번호를 입력하세요")
    
    
        








     



