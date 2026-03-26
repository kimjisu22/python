##1. 레스토랑에서 메뉴를 관리하는 프로그램을 작성하고자 한다. 메뉴는 튜플로 저장되며, 사용자가 원하는 메뉴를 입력하면 메뉴와 가격을 출력하여 원하는 메뉴가 없을 경우 "해당메뉴가 없다"고 출력한다.

menu = (['김밥',3000], ['라면',4000], ['돈까스',7000],['떡뽁이',5000])

order = input("주문할 메뉴를 입력하세요: ")
found = False

for index,item in enumerate(menu):
 
    if item[0]== order:
       found = True
    break
if found:
    print(f"{order}의 가격은 {item[1]}입니다")

else:
    print("해당 메뉴는 없습니다")
        
    
