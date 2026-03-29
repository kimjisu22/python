
#8-1
menu=(
   ["김밥",3000],
   ["라면",4000],
   ["돈까스",8000],
   ["떡뽁이",5000],
    )


flag=False
food=input('주문할 메뉴를 입력하세요 ?')


for item in menu:
  if item[0]== food:
      flag=True
      break
    
if flag:    
   print(f'{food}의 가격은 {item[1]}입니다')
else:
   print('해당메뉴가 없습니다.')

    








