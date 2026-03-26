Sum=0
num=0
 
while num<=100:
 num+=1   
 if num%3 == 0:
    Sum+=num
 else:
    continue
 
 
print('1부터 100까지 숫자중 3의 배수의 합은 ?',Sum)
