
while True:
 print('==== 메뉴 ====')
 print('1. 덧셈 ')
 print('2. 뺄셈 ')
 print('3. 곱셈 ')
 print('4. 나눗셈')
 print('==============')
 
 op=int(input('선택 : '))
 if (op <= 0 or op >=5):
      continue
 else:
      break
     
num1=int(input('첫번째 두수를 입력'))
num2=int(input('두번째 두수를 입력'))
      

if(op==1):
 print(str(num1) + '+' + str(num2) + '=', num1+num2)
elif(op==2):
 print(str(num1) + '-' + str(num2) + '=', num1-num2)
elif(op==3):
 print(str(num1) + '*' + str(num2) + '=', num1*num2)
else:
 print(str(num1) + '/' + str(num2) + '=', num1/num2) if num2>0 else print('0으로 나눌수없습니다.')
 

 
