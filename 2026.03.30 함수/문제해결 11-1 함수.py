flag = True
totalVisitor = 0

def countVistitor():
    global totalVisitor
    totalVisitor += 1

while flag:
    inputData = int(input('1.웹사이트 방문, 2.종료'))

    if inputData == 1:
        countVistitor()
        print('누적방문횟수: ', totalVisitor)
    else:
        flag = False
