totalSum = 0
oddSum = 0
evenSum = 0
num=1
  
while num <=100 :
 if num%2 != 0:
  oddSum +=  num
 else:
  evenSum += num
 num+=1

print('1부터 100까지 짝수의합은 ?',evenSum)
print('1부터 100까지 홀수의합은 ?',oddSum)
