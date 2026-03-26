totalSum = 0
oddSum = 0
evenSum = 0
  
for num in range(1,101):
 if ((num) % 2 != 0):
  oddSum += num
 else:
  evenSum += num

print('1부터 100까지 짝수의합은 ?',evenSum)
print('1부터 100까지 홀수의합은 ?',oddSum)
