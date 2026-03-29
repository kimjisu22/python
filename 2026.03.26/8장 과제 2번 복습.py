menu = (['김밥',2000],['라면',4000],['돈까스',7000],['떡뽁이',5000])

order = input("주문할 메뉴를 입력하세요: ")

found = False

for index, item in enumerate(menu):
    if item[0] == order:
       found = True
    break
if found:
        print(f"{order}의 가격은 {item[1]}입니다")

else:
    print("찾는 메뉴가 없습니다")