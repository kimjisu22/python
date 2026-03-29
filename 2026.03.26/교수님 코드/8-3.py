#8-3
contacts = {
    "철수": "010-1234-5678",
    "영희": "010-9876-5432",
    "민수": "010-5678-1234"
}

while True:
    print("\n1. 연락처 추가")
    print("2. 연락처 조회")
    print("3. 종료")
    choice = input("메뉴를 선택하세요: ")

    if choice == "1":
        name = input("이름을 입력하세요: ")
        phone = input("전화번호를 입력하세요: ")
        contacts[name] = phone
        print(f"{name}의 연락처가 저장되었습니다.")

    elif choice == "2":
        name = input("조회할 이름을 입력하세요: ")
        if name in contacts:
            print(f"{name}의 전화번호: {contacts[name]}")
        else:
            print("해당 연락처가 없습니다.")

    elif choice == "3":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 번호를 입력하세요.")
