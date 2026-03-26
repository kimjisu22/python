size= int(input('리스트 크기 입력:'))

arr=[]

print(f'{size}개의 정수를 입력하세요 ')

for i in range(size):
   arr.append(int(input()))


print(f' 입력하신 리스트는 {arr} 입니다.' )

target=int(input('찾을 값을 입력하세요'))

flag=False

for index, item in enumerate(arr):
    if item == target:
       flag=True
       break


if flag==False:
   print('찾을수 없습니다. ')
else:
   print(f'{target}을 찾았습니다. 인덱스는 {index}입니다.')

  
              
