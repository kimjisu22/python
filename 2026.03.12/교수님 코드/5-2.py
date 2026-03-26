# 1. 사용자로부터 나이를 입력받습니다.
age = int(input("나이를 숫자로 입력하세요: "))

# 2. 여러 조건을 검사하여 요금을 결정합니다.
if age < 8:
    category = "미취학 아동"
    price = "무료"
elif age <= 13:
    category = "초등학생"
    price = "5,000원"
elif  age <= 19:
    category = "중/고등학생"
    price = "10,000원"
elif age <= 64:
    category = "성인"
    price = "20,000원"
else:
    # 65세 이상인 경우 (위의 모든 조건에 해당하지 않을 때)
    category = "어르신 경로우대"
    price = "무료"

# 3. f-포맷을 사용하여 결과를 출력합니다.
print("--- 입장권 정보 ---")
print("고객님은", category, "그룹에 속하며, 입장료는", price,"입니다.")
