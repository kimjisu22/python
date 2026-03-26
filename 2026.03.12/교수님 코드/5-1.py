import random 

ranNum = random.randint(1, 3) 

print('가위, 바위, 보를  선택하세요..')
userNum = int(input('1.가위, 2.바위, 3.보 '))

if (ranNum == 1 and userNum == 2) or (ranNum == 2 and userNum == 3) or (ranNum == 3 and userNum == 1):
    print('컴퓨터: 패, 사용자: 승')
elif (ranNum == 1 and userNum == 3) or (ranNum == 2 and userNum == 1) or (ranNum == 3 and userNum == 2):
    print('컴퓨터: 승, 사용자: 패')
elif ranNum == userNum:
    print('무승부')
    
print('사용자: ', userNum)
print('컴퓨터: ', ranNum) 
