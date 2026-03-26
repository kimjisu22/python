##사용자로부터 금액을 입력 받아 금액을 화폐단위
##(50,000원 10,000원 5,000원 1,000원 500원, 100원 50원 10원)로 나누어
##출력하시오(coin.py)

money = int(input('금액을 입력하세요: '))
won50000 = money // 50000
money = money % 50000

won10000 = money // 10000
money = money % 10000

won5000 = money // 5000
money = money % 5000


won1000 = money // 1000
money = money % 1000

won500 = money // 500
money = money % 500

won100 = money // 100
money = money % 100

won50 = money // 50
money = money % 50

won10 = money // 10
money = money % 10

won1 = money // 1

print('오만원: ', won50000, '매')
print('  만원: ', won10000, '매')
print('오천원: ', won5000, '매')
print('  천원: ', won1000, '매')
print('오백원: ', won500, '개')
print('  백원: ', won100, '개')
print('오십원: ', won50, '개')
print('  십원: ', won10, '개')
print('  일원: ', won1, '개')
